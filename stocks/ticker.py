#!/usr/bin/env python

import ystockquote
import trends
from pandas.io.data import get_data_yahoo

class Ticker:
    'Class for everything related to ticker'

    def __init__(self, symbol):
        self.symbol = symbol
        self.data = None
        self.rsi = None
        self.close_prices = None

    def get_data(self):
        if self.data is not None:
            return self.data
        self.data = get_data_yahoo(self.symbol, '01/01/2012')
        return self.data

    def get_close_prices(self):
        if self.close_prices is not None:
            return self.close_prices

        self.close_prices = []
        for c in self.get_data()['Close']:
            self.close_prices.append(c)
        return self.close_prices

    def get_rsi(self):
        if self.rsi is not None:
            return self.rsi
        self.rsi = trends.relative_strength(self.get_close_prices())
        return self.rsi

    def load_from_file(self, filename):
        return

    def save_to_file(self, filename):
        return

    def load_from_dict(self, dict):
        return 

    def as_dict(self):
        return {
            'symbol' : self.symbol
        }
