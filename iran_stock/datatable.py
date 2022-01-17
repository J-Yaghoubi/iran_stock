
from iran_stock.tools import to_persian
from iran_stock.tools import connect
from iran_stock.exceptions import ConnectionError
from iran_stock.exceptions import TseError
from iran_stock.const import SYMBOLS_TABLE

import os
import re
import pickle
from dataclasses import dataclass
import requests
import pandas as pd
from bs4 import BeautifulSoup

"""
    In this project, we have a pickle file that rules as a database. 
    We store the list of all available Iranians stocks with their Persian_Ticker,
    English_Ticker and Download_ID.
    This information will use when we want to download Price-History.
"""

@dataclass
class Symbol_OBJ:
    id : int
    en_ticker : str
    pr_ticker : str

class Database:
    def __init__(self):
        self.database_patch = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'database' + os.sep + 'db.pickle'
    
    # read Database if exists    

    def read_if_exists(self):
        with open(self.database_patch, 'rb') as f:
            data = pickle.load(f)  
        return data  

    # read Database. 
    # If it is not exists then grab data from tsetmc and make a database then read it    

    def read(self):
        try:
            data = self.read_if_exists()
        except:
            self.update()
            data = self.read_if_exists()
       
        return data    

    # update Database   

    def update(self):

        # Check for internet connection

        if not connect():
            raise ConnectionError() 

        try:
            # Grabbing data

            print('Database updating...')
            url = SYMBOLS_TABLE
            result = requests.get(url).text
            soup = BeautifulSoup(result, 'html.parser')
            table = soup.find('table', {'class': 'table1'})
            table_rows = table.find_all('tr')[1:]
   
            # Scraping and looking for preferred data

            tickers_list = []

            for row in table_rows:
                data = row.find_all('td')
                
                if data[5].text.strip() != '-': 
                    id =  "".join(re.findall('\d{15,20}', str(data[0]))).strip()  
                    en_ticker = data[3].text.strip()
                    pr_ticker = to_persian("".join(re.findall('\((.*?)\)', str(data[0]))))
                    tickers_list.append(Symbol_OBJ(id, en_ticker, pr_ticker)) 

            # Save data to the file(database)

            with open(self.database_patch, "wb") as f:
                pickle.dump(tickers_list, f)  

            print('Database has been updated successfully...')     

        except:
            raise TseError()         


    # Search database for ticker-name and id

    def search(self, ticker):
        id = ''
        en_ticker = ''

        data_table = Database().read()

        for i in range(len(data_table)):
            if data_table[i].pr_ticker == ticker or data_table[i].en_ticker == ticker.upper():
                id = data_table[i].id
                en_ticker = data_table[i].en_ticker
                break

        return  id, en_ticker  


    # Read database and return list of all available stock as dataframe

    def list(self):

        row = []
        data_table = Database().read()

        for i in range(len(data_table)):
            row.append([data_table[i].id, data_table[i].en_ticker, data_table[i].pr_ticker])
        
        df = pd.DataFrame(data=row, columns=['ID', 'English Ticker', 'Persian Ticker'])
        return  df     






