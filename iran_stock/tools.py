
import urllib.request


# replace Arabic character with a Persian one

def to_persian(string):
    return string.replace('ك', 'ک').replace('ي', 'ی').strip()


# Check for internet connection

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False



