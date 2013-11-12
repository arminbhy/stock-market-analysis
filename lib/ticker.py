#!/usr/bin/env python

import ystockquote
import trends
from pandas.io.data import get_data_yahoo

class Ticker:
    'Class for everything related to ticker'

    def __init__(self, symbol):
        self.symbol = symbol

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
