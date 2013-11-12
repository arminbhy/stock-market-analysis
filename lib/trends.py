#!/usr/bin/env python

import numpy as np

def relative_strength(prices, n=14):
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)
 
    for i in range(n, len(prices)):
        delta = deltas[i-1] # cause the diff is 1 shorter
 
        if delta>0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta
    
        up = (up*(n-1) + upval)/n
        down = (down*(n-1) + downval)/n
    
        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)

    return rsi


def moving_average(p, n, type='simple'):
    """
    compute an n period moving average.
    type is 'simple' | 'exponential'
    """

    p = np.asarray(p)
    if type=='simple':
        weights = np.ones(n)
    else:
        weights = np.exp(np.linspace(-1., 0., n))

    weights /= weights.sum()

    a =  np.convolve(p, weights, mode='full')[:len(p)]
    a[:n] = a[n]
    return a


def moving_average_convergence(p, nslow=26, nfast=12):
    """
    compute the MACD (Moving Average Convergence/Divergence) using a fast and slow exponential moving avg'
    return value is emaslow, emafast, macd which are len(p) arrays
    """
    emaslow = moving_average(p, nslow, type='exponential')
    emafast = moving_average(p, nfast, type='exponential')
    return emaslow, emafast, emafast - emaslow

