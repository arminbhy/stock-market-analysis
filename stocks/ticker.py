#!/usr/bin/env python

import ystockquote
import trends
import gfinance
import json
from helper import Helper
from helper import RSIHelper
from pandas.io.data import get_data_yahoo
import os

class Ticker:
    'Class for everything related to ticker'

    def __init__(self, symbol):
        self.symbol = symbol.upper()
        self.quote = None
        self.data = None
        self.rsi = None
        self.close_prices = None
        self.averages = None
        self.gfinance = None

    def get_symbol(self):
        return self.symbol

    def get_stockchart(self):
        return "http://stockcharts.com" + os.popen(
            'curl -H "Connection: keep-alive" '+
            '-H "Cache-Control: max-age=0" '+
            '-H "Accept: text/html;q=0.9,image/webp,*/*;q=0.8" '+
            '-H "User-Agent: Chrome/31.0.1650.57" '+
            '-H "Accept-Encoding: text/html" '+
            '-H "Accept-Language: en-US,en;q=0.8" '+
            'http://stockcharts.com/h-sc/ui?s=' + self.symbol + ' | '+
            'grep id=\\\"chartImg\\\"').read().split("src=\"")[1].split("\" />")[0].strip()

    def get_gfinance(self):
        if self.gfinance is None:
            try:
                self.gfinance = gfinance.GFinance(self.symbol)
            except:
                self.gfinance = None
        return self.gfinance

    def get_quote(self):
        if self.quote is None:
            try:
                self.quote = ystockquote.get_all(self.symbol)
            except:
                self.quote = None
        return self.quote

    def get_data(self):
        if self.data is None:
            try:
                raw_data = get_data_yahoo(self.symbol, '01/01/2012')
                self.data = {}
                for k in raw_data.keys():
                    self.data[k] = []
                    for v in raw_data[k]:
                        self.data[k].append(float(v))
            except:
                self.data = None
        return self.data

    def get_close_prices(self):
        if self.close_prices is None:
            self.close_prices = []
            try:
                for c in self.get_data()['Close']:
                    self.close_prices.append(float(c))
            except:
                self.close_prices = None
        return self.close_prices

    def get_close_price_helper(self):
        return Helper(self.get_close_prices())

    def get_averages(self):
        if self.averages is None:
            try:
                self.averages = trends.averages(self.get_close_prices())
            except:
                self.averages = None
        return self.averages

    def get_signal_helper(self):
        return Helper(self.get_averages()['convergence']['Histogram'])

    def get_rsi(self):
        if self.rsi is None:
            try:
                self.rsi = trends.relative_strength(self.get_close_prices())
            except:
                self.rsi = None
        return self.rsi

    def get_rsi_helper(self):
        return RSIHelper(self.get_rsi())

    def get_last_rsi(self, n=1):
        rsi = self.get_rsi()
        if rsi == None:
            return None
        if n == 1:
            return rsi[len(rsi) - 1]
        else:
            return rsi[len(rsi) - n:]


    def load_from_file(self, dir):
        f = open(dir + '/' + self.symbol, 'r')
        self.load_from_dict( json.load(f) )
        f.close()

    def save_to_file(self, dir):
        f = open(dir + '/' + self.symbol, 'w')
        f.write(json.dumps(self.as_dict()))
        f.close()

    def load_from_dict(self, dict):
        self.symbol = dict['symbol']
        self.rsi = dict['rsi']
        self.data = dict['data']
        self.quote = dict['quote']
        self.close_prices = dict['close_prices']

    def as_dict(self):
        self.get_data()
        self.get_close_prices()
        self.get_rsi()
        self.get_quote()
        self.get_averages()

        return {
            'gfinance' : self.gfinance,
            'symbol' : self.symbol,
            'rsi' : self.rsi,
            'data' : self.data,
            'quote' : self.quote,
            'averages' : self.averages,
            'close_prices' : self.close_prices
        }
