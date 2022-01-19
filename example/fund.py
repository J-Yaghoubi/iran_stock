
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
print(data.value.Ticker)
print(data.value.Title)
print(data.value.Market)
print(data.value.Sector)
print(data.value.EPS)
print(data.value.PE)
print(data.value.SectorPE)
print(data.value.Shares)
print(data.value.FloatingPercent)
print(data.value.MarketCap)
print(data.value.AverageVolume)
print(data.value.BaseVolume)
print(data.value.NAV)