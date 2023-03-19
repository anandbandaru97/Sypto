import ccxt
from pprint import pprint
from datetime import datetime


print('CCXT Version:', ccxt.__version__)
exch='Binance'
exchange = ccxt.binance()
if exchange.has["fetchOHLCV"] != True:
    print('-'*36,' ERROR ','-'*35)
    print('{} does not support fetching OHLC data. Please use another  exchange'.format(exch))
    print('-'*80)
    quit()


symbol="BTC/USDT"
# Check if the symbol is available on the Exchange
exchange.load_markets()
if symbol not in exchange.symbols:
    print('-'*36,' ERROR ','-'*35)
    print('The requested symbol ({}) is not available from {}\n'.format(symbol,exch))
    print('Available symbols are:')
    for key in exchange.symbols:
        print('  - ' + key)
    print('-'*80)
    quit()


t_frame='5m'
# Check requested timeframe is available. If not return a helpful error.
if (not hasattr(exchange, 'timeframes')) or (t_frame not in exchange.timeframes):
    print('-'*36,' ERROR ','-'*35)
    print('The requested timeframe ({}) is not available from {}\n'.format(t_frame,exch))
    print('Available timeframes are:')
    for key in exchange.timeframes.keys():
        print('  - ' + key)
    print('-'*80)
    quit()

# timestamp = int(datetime.datetime.strptime("2018-01-24 11:20:00+00:00", "%Y-%m-%d %H:%M:%S%z").timestamp() * 1000)
# response = exchange.fetch_ohlcv('BTC/USDT', '1m', timestamp, 1)
# pprint(response)
limit =50
startDate = "2022-03-19"
startDate = datetime.strptime(startDate, "%Y-%m-%d")
startDate = int(datetime.timestamp(startDate))
data = exchange.fetch_ohlcv(symbol, t_frame, startDate, limit=limit)
print(data)
