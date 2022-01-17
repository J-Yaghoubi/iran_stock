
from iran_stock.tools import connect
from iran_stock.datatable import Symbol_OBJ
from iran_stock.datatable import Database
from iran_stock.exceptions import ConnectionError
from iran_stock.exceptions import InvalidTicker
from iran_stock.exceptions import TseError
from iran_stock.const import SYMBOLS_PAGE

import re
import requests
from dataclasses import dataclass


"""
    Download fundamental values of given ticker from tsetmc.com and 
    return as Object
"""


@dataclass
class Fundamental:    
    title : str 
    group : str
    evg_volume : int     
    eps : float      
    pe : float
    sector_pe : float
    base_volume : int
    shares : int
    nav : float

    def download_fund(ticker):

        # Check for internet connection

        if not connect():
            raise ConnectionError() 

        # Search for ID and English_ticker in database
            
        id, en_ticker = Database().search(ticker) 

        # If returned value of search is empty then raise exception

        if id == '' or en_ticker == '':
            raise InvalidTicker(ticker)

        # else, read the Tsetmc.com ticker page and return fundamental parameters
           
        else:
            try:
                url = SYMBOLS_PAGE + id 
                response = requests.get(url).text 

                title = re.findall("Title='(.*?)'", response)[0] 
                group = re.findall("LSecVal='(.*?)'", response)[0] 
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

        return Fundamental(title, group, evg_volume, eps, pe, sector_pe, base_volume, shares, nav) 

 


