#!/usr/bin/env python
import numpy

def _direction(a,b):
    if a > b:
        return 1
    if a == b:
        return 0
    return -1

class Helper:
    'Class for everything related to ticker'

    def __init__(self, data):
        self.data = data

    def len(self):
        return len(self.data)

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

    def direction_compareto_average(self, n=14):
        return _direction(
            self.data[len(self.data) - 1],
            numpy.mean(self.data[len(self.data) - n:]))

    def direction_since_max_or_min(self, n=14):
        return self.direction_compareto_average(
            min(self.days_since_max(n), 
                self.days_since_min(n)) + 1)

class RSIHelper(Helper):
    def status(self):
        v = self.data[len(self.data) - 1]
        if v > 70:
            return 'Over-Bought'
        if v < 30:
            return 'Over-Sold'
        return 'NA'

