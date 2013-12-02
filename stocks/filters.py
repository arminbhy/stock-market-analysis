#!/usr/bin/env python

class Filter:
    def __init__(self, tickers):
        self.tickers = tickers

    def filter(self, _min=None):
        return self.tickers

    def excluded(self, _min=None):
        return self.tickers

class VolumeFilter(Filter):
    def filter(self, _min=500000):
        filtered = []
        for t in self.tickers:
            if t.get_quote()['avg_daily_volume'] >= _min:
                filtered.append(t)
        return filtered

    def excluded(self, _min=500000):
        excluded = []
        for t in self.tickers:
            if t.get_quote()['avg_daily_volume'] < _min:
                excluded.append(t)
        return excluded

def strCapToCap(cap):
    if 'M' in cap:
        return float(cap.split('M')[0]) * 1000 * 1000
    if 'B' in cap:
        return float(cap.split('B')[0]) * 1000 * 1000 * 1000
    return cap

class MarketCapitalFilter(Filter):
    def filter(self, _min="500M"):
        filtered = []
        for t in self.tickers:
            if strCapToCap(t.get_quote()['market_cap']) >= strCapToCap(_min):
                filtered.append(t)
        return filtered

    def excluded(self, _min="500M"):
        excluded = []
        for t in self.tickers:
            if strCapToCap(t.get_quote()['market_cap']) < strCapToCap(_min):
                excluded.append(t)
        return excluded

# TODO Something more meaningful :)
class PotentialFilter(Filter):
    def filter(self):
        tickers = []
        for t in self.tickers:
            try:
                if t.get_calculated_pe() < 100:
                    rsi = t.get_rsi_helper()
                    signal = t.get_signal_helper()
                    if rsi.last_value() < 35:
                        if signal.last_value() > 0 and signal.direction() > 0:
                            tickers.append(t)
            except:
                pass
        return tickers