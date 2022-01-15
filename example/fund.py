
import iran_stock as tse

# Get historical data by Persian-Ticker
data = tse.fund('شبندر')

# Get historical data by English-Ticker
data = tse.fund('PNBA')

# Get list off historical data by Persian-Ticker
tickers = ['شبندر', 'وبرق']
data = tse.fund(tickers)
print(data[0])
print(data[1])

# Get list off historical data by English-Ticker
tickers = ['SEIP', 'PNBA']
data = tse.fund(tickers)
print(data[0])
print(data[1])

# Get access to special parameter of fundamental values
data = tse.fund('شبندر')
print(data.title)
print(data.group)
print(data.evg_volume)
print(data.eps)
print(data.pe)
print(data.sector_pe)
print(data.base_volume)
print(data.shares)
print(data.nav)




