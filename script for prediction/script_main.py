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

callsDF = pd.DataFrame(calls, columns=['date', 'sum of calls'])
callsDF['date'] = pd.to_datetime(callsDF['date'])
callsDF.set_index('date', inplace=True)

test = sm.tsa.adfuller(callsDF['sum of calls'])
print(test[0] < test[4]['5%'])

fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(callsDF.values.squeeze(), lags=25, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(callsDF, lags=25, ax=ax2)

model = sm.tsa.ARIMA(callsDF, order=(1, 1, 1), freq='D').fit(full_output=True, disp=0)
print(model.summary())

pred = model.predict('2017-02-28', '2017-03-31', typ='levels')

callsDF.plot(figsize=(12, 6))
pred.plot(style='r--', label="predict")

time_series = callsDF['sum of calls']
time_series.rolling(30).mean().plot(label="rolling mean per month")

print(pred)
plt.legend()
plt.show()
