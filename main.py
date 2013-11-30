from stocks import PreDefinedSymbols
from stocks import Ticker
from stocks import PreDefinedSymbols
from time import sleep
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == 'main':
            print 'main'

        if sys.argv[1] == 'update':
            PreDefinedSymbols.relevant.update()

        if sys.argv[1] == 'dev':
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

    print 'Done'