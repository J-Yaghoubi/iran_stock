

# Table of all available stock
SYMBOLS_TABLE = 'http://tsetmc.com/Loader.aspx?ParTree=151114'

# pre-address for access to current data of tickers
SYMBOLS_PAGE  = 'http://tsetmc.com/Loader.aspx?ParTree=151311&i='

# pre-address for download historical price data
DOWNLOAD_URL  = 'http://www.tsetmc.com/tsev2/data/Export-txt.aspx?t=i&a=1&b=0&i='
 

# The name that will use to change dataframe index-name
DATAFRAME_INDEX_NAME =  ['Data']

# The list that will use to change dataframe default columns-name
DATAFRAME_COLUMNS_NAME =  ['Ticker', 'First', 'High', 'Low', 'Close', 'Value', 'Vol', 'OpenInt', 'TF', 'Open', 'Last']