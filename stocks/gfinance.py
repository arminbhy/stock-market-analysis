#!/usr/bin/env python

import urllib2
import urllib
from pyquery import PyQuery
import time
from datetime import date, timedelta

class GFinance:
    'Class for extracting google finance information'

    def __init__(self, symbol):
        self.symbol = symbol
        self.html = None
        self.desc = None
        self.events = None

    def get_html(self):
        if self.html is None:
            req = urllib2.Request('https://www.google.com/finance?q=:' + self.symbol)
            html_data = urllib2.urlopen(req).readlines()
            self.html = ''.join(html_data)
        return self.html

    def get_description(self):
        if self.desc is None:
            try:
                self.desc = PyQuery(self.get_html()).find('.companySummary').text().encode('ascii', 'ignore')
            except:
                self.desc = ""
        return self.desc

    def get_events(self):
        if self.events is None:
            result = []
            children = PyQuery(self.get_html()).find('.events').children()
            for i in range(0, len(children)-1):
                event = PyQuery(children.eq(i).html()).children()
                result.append([
                    time.strptime(event.eq(0).text(), "%b %d, %Y"),
                    event.eq(1).text().replace('\n',' '),
                    ])
            self.events = result
        return self.events

    def get_events_str(self):
        events = []
        d=date.today()-timedelta(days=7)
        for e in self.get_events():
            if e[0] > d.timetuple():
                events.append({
                    'time' : time.strftime("%Y-%m-%d", e[0]),
                    'event' : e[1].encode('ascii', 'ignore')})
        return events
