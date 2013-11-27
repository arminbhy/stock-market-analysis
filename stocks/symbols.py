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