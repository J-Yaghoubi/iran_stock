
from iran_stock.tools import connect
from iran_stock.datatable import Symbol_OBJ
from iran_stock.datatable import Database
from iran_stock.exceptions import ConnectionError
from iran_stock.exceptions import InvalidTicker
from iran_stock.exceptions import TseError
from iran_stock.const import SYMBOLS_PAGE
from iran_stock.const import FUNDAMENTHAL_INDEX_NAME
from iran_stock.const import REAL_TIME_DATA

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


    def convert_type(self, data, change_type):
        """ Convert craped data to standard data-type """

        if data != None and  data != '':
            return change_type(data)
        return None      
           

    def download_fund(self):
        """ Scraping data from tsetmc.com  """    

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
                # grabbing data from tsetmc.com
                url = SYMBOLS_PAGE + id 
                response = requests.get(url).text 
                real_time_data = requests.get(REAL_TIME_DATA.format({id})).text.split(',') 

                # adjusted close
                adjusted_close = int(real_time_data[3])
                adjusted_close = self.convert_type(adjusted_close, float)

                # ticker, title, market and sector
                ticker = re.findall("LVal18AFC='(.*?)'", response)[0].strip() 
                title = re.findall("Title='(.*?)'", response)[0].split('-')[0].strip()
                market = re.findall("Title='(.*?)'", response)[0].split('-')[1].strip()
                sector = re.findall("LSecVal='(.*?)'", response)[0].strip()

                # eps
                eps = re.findall("EstimatedEPS='(.*?)'", response)[0]
                eps = self.convert_type(eps, float)

                # sector p/e           
                sector_pe = re.findall("SectorPE='(.*?)'", response)[0] 
                sector_pe = self.convert_type(sector_pe, float)

                # total shares
                shares = re.findall("ZTitad=(.*?),", response)[0]  
                shares = self.convert_type(shares, int)

                # floating shares in percentage
                floating_shares = re.findall("KAjCapValCpsIdx='(.*?)'", response)[0]  
                floating_shares = self.convert_type(floating_shares, float)

                # average volume
                evg_volume = re.findall("QTotTran5JAvg='(.*?)'", response)[0]
                evg_volume = self.convert_type(evg_volume, int)
               
                # base volume
                base_volume = re.findall("BaseVol=(.*?),", response)[0]
                base_volume = self.convert_type(base_volume, int)

                # nav
                nav = re.findall("NAV='(.*?)'", response)[0]
                nav = self.convert_type(nav, float)

                # calculate pe if we have information of eps and adjusted_close
                if eps != None and adjusted_close != None:
                    pe = round(adjusted_close / eps,1)
                else:
                    pe = None       

                # calculate market_cap if we have information adjusted_close
                if adjusted_close != None:
                    market_cap = int(shares * adjusted_close)
                else:
                    market_cap = None     

            except:
                raise TseError()    

        # create Pandas-DataFrame from scraped data
        fundamenthal_data = [ticker, title, market, sector, eps, pe, sector_pe, shares, floating_shares, market_cap, evg_volume, base_volume, nav]
        df = pd.DataFrame(data=fundamenthal_data, index=FUNDAMENTHAL_INDEX_NAME, columns= ['value'])
        
        # return fundamental data as dataframe
        return  df  

 


