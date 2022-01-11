from matplotlib.pyplot import savefig, title, ylabel
import pandas as pd
import requests
from datetime import date, timedelta
import mplfinance as mpf

def candles_graph(start_date, currency1, currency2='USDT', time_interval='1h'):
    url = f'https://dev-api.shrimpy.io/v1/exchanges/binance/candles'
    payload = {'interval': time_interval, 'baseTradingSymbol': currency1,
               'quoteTradingSymbol': currency2, 'startTime': start_date}

    response = requests.get(url, params=payload)
    data = response.json()

    open_price, close_price, high_price, low_price, time_price = [], [], [], [], []

    for candle in data:
        open_price.append(float(candle['open']))
        high_price.append(float(candle['high']))
        low_price.append(float(candle['low']))
        close_price.append(float(candle['close']))
        time_price.append(candle['time'])

    raw_data = {'Date': pd.DatetimeIndex(time_price),
                'Open': open_price,
                'High': high_price,
                'Low': low_price,
                'Close': close_price}

    df = pd.DataFrame(raw_data).set_index('Date')

    mpf.plot(df, type='candle', style='yahoo', title=f'{currency1}/{currency2}', ylabel=f'{currency2}', savefig='src/graph')
    #mpf.show()

    #return df

def return_days_ago():
    current_day = date.today() - timedelta(4)
    return current_day
    