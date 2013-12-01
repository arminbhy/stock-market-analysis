from stocks import PreDefinedSymbols
from stocks import Ticker
from stocks import VolumeFilter
from stocks import MarketCapitalFilter
from time import sleep
import sys

def update(argv):
    PreDefinedSymbols.relevant.update()



def filter(argv):
    tickers = PreDefinedSymbols.relevant.get_loaded_tickers()
    ignore = []
    for t in VolumeFilter(tickers).excluded():
        ignore.append(t.get_symbol())

    for t in MarketCapitalFilter(tickers).excluded():
        ignore.append(t.get_symbol())

    print 'Adding ', len(ignore), 'Symbols to ignore list'
    PreDefinedSymbols.ignore.append(ignore)



def main(argv):
    PreDefinedSymbols.relevant.get_loaded_tickers()
    print 'main'



def dev(argv):
    h = Ticker('OGE').get_rsi_helper()
    print 'min', h.min()
    print 'days_since_min', h.days_since_min()
    print 'max', h.max()
    print 'days_since_max', h.days_since_max()
    print 'direction', h.direction()
    print 'direction_since_max_or_min', h.direction_since_max_or_min()
    try:
        print 'status', h.status()
    except:
        print 'status', 'No Status'



if __name__ == "__main__":
    if len(sys.argv) >= 2:
        globals()[sys.argv[1]](sys.argv)


