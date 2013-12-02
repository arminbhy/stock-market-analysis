#!/usr/bin/env python
import numpy
import pystache

def _direction_to_str(direction):
    if direction == 1:
        return "Positive"
    if direction == -1:
        return "Negative"
    return "None"

def _direction(a,b):
    if a > b:
        return 1
    if a == b:
        return 0
    return -1

def _rsi(v):
    if v > 70:
        return 'Over-Bought'
    if v < 30:
        return 'Over-Sold'
    if v > 60:
        return 'Almost-Over-Bought'
    if v < 40:
        return 'Almost-Over-Sold'
    return 'Avearge'

class Helper:
    'Class for everything related to ticker'

    def __init__(self, data):
        self.data = data

    def len(self):
        return len(self.data)

    def last_value(self):
        return self.data[len(self.data) - 1]

    def min(self, n=14):
        return min(self.data[len(self.data) - n:])

    def max(self, n=14):
        return max(self.data[len(self.data) - n:])

    def days_since_min(self, n=14):
        group = self.data[len(self.data) - n:]
        group.reverse()
        return group.index(self.min(n))

    def days_since_max(self, n=14):
        group = self.data[len(self.data) - n:]
        group.reverse()
        return group.index(self.max(n))

    def direction(self):
        return _direction(
            self.data[len(self.data) - 1],
            self.data[len(self.data) - 2] )

    def direction_str(self):
        return _direction_to_str(self.direction())

    def direction_compareto_average(self, n=14):
        return _direction(
            self.data[len(self.data) - 1],
            numpy.mean(self.data[len(self.data) - n:]))

    def direction_since_max_or_min(self, n=14):
        return self.direction_compareto_average(
            min(self.days_since_max(n), 
                self.days_since_min(n)) + 1)

    def report(self, n=14):
        return pystache.render('Direction {{direction}}, Value {{value}}, {{n}}D Min {{min}}, Max {{max}}, Days Since Min {{since_min}}, Max {{since_max}}', {
            'n' : n,
            'direction' : _direction_to_str(self.direction()),
            'value' : round(self.data[len(self.data) - 1],2),
            'min' : round(self.min(n),2),
            'max' : round(self.max(n),2),
            'since_min' : self.days_since_min(n),
            'since_max' : self.days_since_max(n)
            })

class RSIHelper(Helper):
    def status(self):
        return _rsi(self.data[len(self.data) - 1])

    def min_status(self, n=14):
        return _rsi(self.min(n))

    def max_status(self, n=14):
        return _rsi(self.max(n))

