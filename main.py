from stocks import PreDefinedSymbols
from stocks import Ticker
from stocks import VolumeFilter
from stocks import MarketCapitalFilter
from stocks import PotentialFilter
from time import sleep
import sys
from stocks import mailer
import datetime

# ----------------------------------UPDATE-------------------------------------
def update(argv):
    PreDefinedSymbols.relevant.update()

# ----------------------------------UPDATE-------------------------------------
def update_owned(argv):
    PreDefinedSymbols.own.update()

# ----------------------------------FILTER-------------------------------------
def filter(argv):
    tickers = PreDefinedSymbols.relevant.get_loaded_tickers()
    ignore = []
    for t in VolumeFilter(tickers).excluded():
        ignore.append(t.get_symbol())

    for t in MarketCapitalFilter(tickers).excluded():
        ignore.append(t.get_symbol())

    print 'Adding ', len(ignore), 'Symbols to ignore list'
    PreDefinedSymbols.ignore.append(ignore)

# ----------------------------------OWN---------------------------------------
def own(argv):
    html = '<BR><h1>Own</h1><BR>'
    for t in PreDefinedSymbols.own.get_loaded_tickers():
        print t.get_symbol()
        html += t.as_html()
    mailer.send('Stock Report ' + str(datetime.datetime.now()), html)

# ----------------------------------MAIN--------------------------------------
def main(argv):

    html = '<BR><h1>Own</h1><BR>'
    for t in PreDefinedSymbols.own.get_loaded_tickers():
        print t.get_symbol()
        html += t.as_html()

    html += '<BR><h1>Watch</h1><BR>'
    for t in PreDefinedSymbols.watch.get_loaded_tickers():
        print t.get_symbol()
        html += t.as_html()

    html += '<BR><h1>Potentials</h1><BR>'
    for t in PotentialFilter(PreDefinedSymbols.relevant.get_loaded_tickers()).filter():
        print t.get_symbol()
        html += t.as_html()

    mailer.send('Stock Report ' + str(datetime.datetime.now()), html)

# -----------------------------------DEV--------------------------------------
def dev(argv):
    for t in PotentialFilter(PreDefinedSymbols.relevant.get_loaded_tickers()).filter():
        print t.get_symbol()


# -------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        globals()[sys.argv[1]](sys.argv)


