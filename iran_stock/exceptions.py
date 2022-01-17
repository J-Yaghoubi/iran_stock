

class InvalidTicker(Exception):
    def __init__(self, message):
        super().__init__(f'Sorry, {self.ticker} Not found in database. Please correct the input spell.\n'
                          'If you are sure about your spell, please update the database...')

class InvalidFormat(Exception):
    def __init__(self):
        super().__init__('The imput must be string for single Ticker and List for multiple Tickers...')  


class ConnectionError(Exception):
    def __init__(self):
        super().__init__(f'Somethings goes wrong...\n'
                          'We failed to establish an internet connection...')    


class TseError(Exception):
    def __init__(self):
        super().__init__(f'Somethings goes wrong...\n'
                          'We failed to access tsetms.com data. Please try again later...')            