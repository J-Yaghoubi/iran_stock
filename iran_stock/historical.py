
from iran_stock.tools import connect
from iran_stock.datatable import Symbol_OBJ
from iran_stock.datatable import Database
from iran_stock.exceptions import ConnectionError
from iran_stock.exceptions import InvalidTicker
from iran_stock.exceptions import TseError
from iran_stock.const import DOWNLOAD_URL
from iran_stock.const import DATAFRAME_COLUMNS_NAME
from iran_stock.const import DATAFRAME_INDEX_NAME

import os
import requests
import pandas as pd


"""
    Download historical price of given ticker from tsetmc.com and 
    return as Pandas dataframe
"""

class History:

    def __init__(self, ticker, start, end):
        self.ticker = ticker
        self.start = start
        self.end = end

    def download_history(self):

        # Check for internet connection

        if not connect():
            raise ConnectionError()  
                    
        # Search for ID and English_ticker in database

        id, en_ticker = Database().search(self.ticker) 

        # If returned value of search is empty then call the user      

        if id == '' or en_ticker == '':
            raise InvalidTicker() 

        # else, download historical price
            
        else:
            
            # download content

            try:            
                url = DOWNLOAD_URL + id 
                response = requests.get(url).text  
            except:
                raise TseError()       

            # save to temp directory

            cache = (os.getenv("TEMP") if os.name=="nt" else "/tmp") + os.path.sep + en_ticker + '.csv'   
            with open(cache, "w") as f:
                f.write(response)

            # read and convert to dataframe    

            df = pd.read_csv(cache)
            df.set_index('<DTYYYYMMDD>', inplace= True) 
            df.index= pd.to_datetime(df.index, format='%Y%m%d')
            df.columns = DATAFRAME_COLUMNS_NAME
            df.index.names = DATAFRAME_INDEX_NAME    
            df = df[(df.index > self.start) & (df.index < self.end)]
                    
        return df         





                               

            
            
