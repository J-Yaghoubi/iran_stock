
import iran_stock as tse

# Get historical data by Persian-Ticker
data = tse.get('شبندر')

# Get historical data by English-Ticker
data = tse.get('PNBA')

# Get list off historical data by Persian-Ticker
tickers = ['شبندر', 'وبرق']
data = tse.get(tickers)
print(data[0])
print(data[1])

# Get list off historical data by English-Ticker
tickers = ['SEIP', 'PNBA']
data = tse.get(tickers)
print(data[0])
print(data[1])

# Get historical data by English-Ticker and restricted the start of data
# from 2012-01-29 to the last data
data = tse.get('PNBA', start='2012-01-29')

# Get historical data by English-Ticker and restricted the start and end of data
# from 2012-01-29 to 2022-01-01
data = tse.get('PNBA', start='2012-01-29', end='2022-01-01')


