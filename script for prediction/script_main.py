from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from call_model import Call
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

engine = create_engine('sqlite:///calls.sqlite3', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

calls = session.query(Call.callTimeStart, func.count(Call.callTimeStart))\
    .group_by(func.strftime('%Y-%m-%d', Call.callTimeStart))\
    .all()

for call in calls:
    print(call)

callsDF = pd.DataFrame(calls, columns=['date', 'sum of calls'])
callsDF['date'] = pd.to_datetime(callsDF['date'])
callsDF.set_index('date', inplace=True)

resampled = callsDF.resample('W').mean()

test = sm.tsa.adfuller(resampled['sum of calls'])
print(test[0] < test[4]['5%'])

# fig = plt.figure(figsize=(12,8))
# ax1 = fig.add_subplot(211)
# fig = sm.graphics.tsa.plot_acf(resampled.values.squeeze(), lags=25, ax=ax1)
# ax2 = fig.add_subplot(212)
# fig = sm.graphics.tsa.plot_pacf(resampled, lags=25, ax=ax2)



src_data_model = resampled[:'2016-10-25']
model = sm.tsa.SARIMAX(src_data_model, order=(1, 1, 1), freq='W').fit(full_output=True, disp=0)
print(model.summary())

#pred = model.predict('2017-02-10', '2017-02-22', typ='levels')

resampled.plot(figsize=(12, 6))
#pred.plot(style='r--')

plt.show()
# time_series = callsDF['sum of calls']
# time_series.rolling(30).mean().plot(label="rolling mean per month")
# time_series.plot()
# plt.show()