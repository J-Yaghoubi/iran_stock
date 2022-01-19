
from iran_stock.historical import History
from iran_stock.fundamental import Fundamental
from iran_stock.datatable import Symbol_OBJ
from iran_stock.datatable import Database
from iran_stock.tools import to_persian
from iran_stock.exceptions import InvalidFormat


def get(ticker, start='1980-01-01', end='2090-01-01'):
    """
        Get historical price for one ticker or list of tickers
    """

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
        raise InvalidFormat()


def fund(ticker):
    """
        Get fundamenthal values for one ticker or list of tickers
    """ 

    # String
    if isinstance(ticker, str):
       return  Fundamental(to_persian(ticker)).download_fund()

    # List
    elif isinstance(ticker, list):
        tickers_data = []
        for i in range(len(ticker)):
           tickers_data.append(Fundamental(to_persian(ticker[i])).download_fund()) 
        return tickers_data

    # Wrong format
    else:
        raise InvalidFormat()


def update():
    """
        Update the database that holds the list of all available stocks
    """
    Database().update()


def check():
    """
        Read Database and return list of all available stock as Pandas-dataframe
    """
    return Database().list()

