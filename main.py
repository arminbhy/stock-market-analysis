from stocks import PreDefinedSymbols
from stocks import Ticker
from stocks import PreDefinedSymbols
from time import sleep
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == 'update':
            PreDefinedSymbols.relevant.update()
    print 'Done'