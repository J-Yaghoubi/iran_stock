
import urllib.request


def to_persian(string):
    """ replace Arabic character with a Persian one """

    return string.replace('ك', 'ک').replace('ي', 'ی').strip()



def connect(host='http://google.com'):

    """ 
        Check for internet connection 
        tsetmc.com has banned ping requests, so we check internet connection by google.com
    """

    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False



