#!/usr/bin/env python

import urllib2
import urllib
from pyquery import PyQuery

class GFinance:
    'Class for extracting google finance information'

    def __init__(self, symbol):
        self.symbol = symbol
        self.html = None

    def get_html(self):
        if self.html is not None:
            return self.html

        req = urllib2.Request('https://www.google.com/finance?q=:' + self.symbol)
        html_data = urllib2.urlopen(req).readlines()
        self.html = ''.join(html_data)
        return self.html

    def get_description(self):
        return PyQuery(self.get_html()).find('.companySummary').text()

    def get_events(self):
        # TODO: Parse the events
        #PyQuery(self.get_html()).find('.sfe-section').children().next().html()
        return None

    def get_quotes(self):
        # TODO: Parse the quotes
        #$('.quotes')
        return None
        
