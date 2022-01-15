
from historical import History
from fundamental import Fundamental
from datatable import Symbol_OBJ
from datatable import Database
from tools import to_persian
import exceptions

"""
    Get historical price for one ticker or list of tickers
"""

def get(ticker, start='1980-01-01', end='2090-01-01'):

    # String
    if isinstance(ticker, str):
       return  History(to_persian(ticker), start, end).download_history()

    # List
    elif isinstance(ticker, list):
        tickers_data = []
        for i in range(len(ticker)):
           tickers_data.append(History(to_persian(ticker[i]), start, end).download_history())  
        return tickers_data

    # Wrong format
    else:
        raise exceptions.InvalidFormat()

"""
    Get fundamenthal values for one ticker or list of tickers
""" 

def fund(ticker):

    # String
    if isinstance(ticker, str):
       return  Fundamental.download_fund(to_persian(ticker))

    # List
    elif isinstance(ticker, list):
        tickers_data = []
        for i in range(len(ticker)):
           tickers_data.append(Fundamental.download_fund(to_persian(ticker[i])))  
        return tickers_data

    # Wrong format
    else:
        raise exceptions.InvalidFormat()

"""
    Update the database that holds the list of all available stocks
"""

def update():
    Database().update()

"""
    Read Database and return list of all available stock as Pandas-dataframe
"""

def check():
    return Database().list()
