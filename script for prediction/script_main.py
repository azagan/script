import database
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


def main():
    callsDB = database.CallsDataBase('sqlite:///calls.sqlite3')
    calls = callsDB.getCountGroupByDay()

    # Конвертируем в DataFrames
    callsDF = pd.DataFrame(calls, columns=['date', 'sum of calls'])
    callsDF['date'] = pd.to_datetime(callsDF['date'])
    callsDF.set_index('date', inplace=True)

    # Проводим тест Дики-Фуллера
    test = sm.tsa.adfuller(callsDF['sum of calls'])
    print(' Ряд стационарен и не имеет единичных корней: ', test[0] < test[4]['5%'])

    # Строим графики ACF и PACF
    fig = plt.figure(figsize=(12, 9))
    ax1 = fig.add_subplot(311)
    fig = sm.graphics.tsa.plot_acf(callsDF.values.squeeze(), lags=25, ax=ax1)
    ax2 = fig.add_subplot(312)
    fig = sm.graphics.tsa.plot_pacf(callsDF, lags=25, ax=ax2)

    model = sm.tsa.ARIMA(callsDF, order=(1, 1, 1), freq='D').fit(full_output=True, disp=0)
    print(model.summary())

    prediction = model.predict('2017-02-28', '2017-03-31', typ='levels')
    print(prediction)

    ax3 = fig.add_subplot(313)
    fig = prediction.plot(style='r--', label="prediction", ax=ax3)
    fig = callsDF.plot(ax=ax3)

    time_series = callsDF['sum of calls']
    fig = time_series.rolling(30).mean().plot(label="rolling mean per month", ax=ax3)

    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()


