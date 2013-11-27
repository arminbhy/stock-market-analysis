import sys
import os

class Symbols:
    'Class for extracting symbols from a file'

    def __init__(self, group):
        self.group = group
        self.symbols = []
        for l in open('symbols/' + group, 'r'):
            self.symbols.append(l.strip())

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

class PreDefinedSymbols:
    all = Symbols('all')
    ignore = Symbols('ignore')
    own = Symbols('own')
    watch = Symbols('watch')
    relevant = all.exclude(ignore).include(own).include(watch)
