#!/usr/bin/env python

import urllib2
import urllib
from pyquery import PyQuery

class Event:
    'Class for stock event information'

    def __init__(self, symbol):
        self.symbol = symbol
        self.data = None

    def get_data(self):
        if self.data != None:
            return self.data

        req = urllib2.Request('http://www.motleyfoolp.idmanagedsolutions.com/stocks/events/symbol/' + self.symbol)
        html_data = urllib2.urlopen(req).readlines()

        self.data = []

        row = []
        for c in PyQuery(PyQuery(''.join(html_data)).find('#idmswrapper').children().next().html()).find('td').contents():
            row.append(c.strip())
            if len(row) == 3:
                self.data.append(row)
                row = []

        return self.data

