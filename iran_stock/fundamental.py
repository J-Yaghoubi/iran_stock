
from iran_stock.tools import connect
from iran_stock.datatable import Symbol_OBJ
from iran_stock.datatable import Database
from iran_stock.exceptions import ConnectionError
from iran_stock.exceptions import InvalidTicker
from iran_stock.exceptions import TseError
from iran_stock.const import SYMBOLS_PAGE
from iran_stock.const import FUNDAMENTHAL_COLUMNS_NAME

import re
import pandas as pd
import requests

"""
    Download fundamental values of given ticker from tsetmc.com and 
    return as Dataframe
"""

class Fundamental:  

    def __init__(self, ticker):
        self.ticker = ticker

    def download_fund(self):

        # Check for internet connection

        if not connect():
            raise ConnectionError() 

        # Search for ID and English_ticker in database
            
        id, en_ticker = Database().search(self.ticker) 

        # If returned value of search is empty then raise exception

        if id == '' or en_ticker == '':
            raise InvalidTicker(self.ticker)

        # else, read the Tsetmc.com ticker page and return fundamental parameters
           
        else:
            try:
                url = SYMBOLS_PAGE + id 
                response = requests.get(url).text 

                ticker = re.findall("LVal18AFC='(.*?)'", response)[0] 
                title = re.findall("Title='(.*?)'", response)[0] 
                sector = re.findall("LSecVal='(.*?)'", response)[0] 
                evg_volume = re.findall("QTotTran5JAvg='(.*?)'", response)[0] 
                eps = re.findall("EstimatedEPS='(.*?)'", response)[0] 
                if eps != '':
                    pe = round((float(re.findall("PSGelStaMax='(.*?)'", response)[0]) + float(re.findall("PSGelStaMin='(.*?)'", response)[0]))/ 2 / float(eps),1) 
                else:
                    pe = '0'         
                sector_pe = re.findall("SectorPE='(.*?)'", response)[0]     
                base_volume = re.findall("BaseVol=(.*?),", response)[0] 
                shares = re.findall("ZTitad=(.*?),", response)[0]                    
                nav = re.findall("NAV='(.*?)'", response)[0]   
            except:
                raise TseError()    

        # return fundamental data as dataframe        

        fundamenthal_data = [[ticker, title, sector, evg_volume, eps, pe, sector_pe, base_volume, shares, nav]]
        df = pd.DataFrame(data=fundamenthal_data, columns= FUNDAMENTHAL_COLUMNS_NAME)
       
        return  df.to_string(index = False)      

 


