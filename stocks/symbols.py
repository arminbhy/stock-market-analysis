import sys
import os
from ticker import Ticker
from time import sleep

class Symbols:
    'Class for extracting symbols from a file'

    def __init__(self, group):
        self.group = group
        self.symbols = []
        self.tickers = None
        for l in open('symbols/' + group, 'r'):
            self.symbols.append(l.strip())

    def get_tickers(self):
        if self.tickers is None:
            tickers = []
            for sym in self.symbols:
                tickers.append(Ticker(sym))
            self.tickers = tickers
        return self.tickers

    def get_loaded_tickers(self, dir_name='data'):
        tickers = self.get_tickers()
        loaded_tickers = []
        for t in tickers:
            try:
                t.load_from_file(dir_name)
                loaded_tickers.append(t)
            except:
                pass
        return loaded_tickers

    def append(self, tickers):
        f = open('symbols/' + self.group, 'a')
        for t in tickers:
            if t not in self.symbols:
                f.write(t + '\n')
                self.symbols.append(t)
        f.close()


    def get_symbols(self):
        return self.symbols

    def get_group(self):
        return self.group

    def exclude(self, symbols):
        self.symbols = [x for x in self.symbols if x not in symbols.get_symbols()]
        return self

    def include(self, symbols):
        for sym in symbols.get_symbols():
            if sym not in self.symbols:
                self.symbols.append(sym)
        return self

    def update(self, dir_name='data', delay=0.5):
        for sym in self.get_symbols():
            Ticker(sym).save_to_file(dir_name)
            sleep(delay)

class PreDefinedSymbols:
    all = Symbols('all')
    ignore = Symbols('ignore')
    own = Symbols('own')
    watch = Symbols('watch')
    relevant = all.exclude(ignore).include(own).include(watch)
