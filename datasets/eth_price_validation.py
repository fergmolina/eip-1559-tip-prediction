import ccxt
import datetime
import pytz
import pandas as pd

def get_ohlcv_data(symbol, start, array_price, timeframe='1h'):
    """
    This uses CCXT to fetch raw ohlcv data from the exchange
    """
    try:
        price_data = binance.fetch_ohlcv(symbol, timeframe, start, limit=1000)
        inserted = len(price_data)
        price_data = array_price + price_data
        return price_data, inserted
    except Exception as e:
        print(e)
    return 





binance = ccxt.binance()

binance.load_markets()

lp = 'ETH/USDT'
ohlcv = []
start_date = datetime.datetime(2022, 8, 7, 0, 50, tzinfo = pytz.utc)
end_date = datetime.datetime(2022, 9, 1, 7, 35, tzinfo = pytz.utc)
difference = end_date - start_date
print(difference)
start_date_int = binance.parse8601(str(start_date))
while start_date <= end_date:
    
    print(start_date)
    print(lp)
    ohlcv, hours_added = get_ohlcv_data(symbol=lp, start=start_date_int, array_price = ohlcv)

    start_date = start_date + datetime.timedelta(hours=hours_added)
    if (start_date > end_date):
        start_date = start_date + datetime.timedelta(hours=1)

    start_date_int = binance.parse8601(str(start_date))

eth_price = pd.DataFrame(columns = ['datetime', 'eth_price'])
for row in ohlcv:
    eth_price = eth_price.append({'datetime': datetime.datetime.utcfromtimestamp(row[0] / 1e3), 'eth_price': row[4]}, ignore_index=True)

print(eth_price)
eth_price.to_csv('eth_price_validation.csv')
