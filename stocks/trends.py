#!/usr/bin/env python

import numpy as np

def make_float(values):
    ret_values = []
    for v in values:
        ret_values.append(float(v))
    return ret_values

def raw_moving_average(x,n, type='simple'):
    """
    compute an n period moving average.
    type is 'simple' | 'exponential'
    """

    x = np.asarray(x)
    if type=='simple':
        weights = np.ones(n)
    else:
        weights = np.exp(np.linspace(-1., 0., n))

    weights /= weights.sum()


    a =  np.convolve(x, weights, mode='full')[:len(x)]
    a[:n] = a[n]
    return a

def moving_average(x, n, type='simple'):
    try:
        return make_float(raw_moving_average(x, n, type))
    except:
        return None

def relative_strength(prices, n=14):
    """
    compute the n period relative strength indicator
    http://stockcharts.com/school/doku.php?id=chart_school:glossary_r#relativestrengthindex
    http://www.investopedia.com/terms/r/rsi.asp
    """

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

    return make_float(rsi)

def moving_average_convergence(x, nslow=26, nfast=12):
    """
    compute the MACD (Moving Average Convergence/Divergence) using a fast and slow exponential moving avg'
    return value is emaslow, emafast, macd which are len(x) arrays
    """
    try:
        emaslow = raw_moving_average(x, nslow, type='exponential')
        emafast = raw_moving_average(x, nfast, type='exponential')
        macd = emafast - emaslow
        signal = raw_moving_average(macd, 9, type='exponential')
        return {
            '26EMA' : make_float(emaslow), 
            '12EMA' : make_float(emafast), 
            'MACD' : make_float(macd), 
            'Signal' : make_float(signal), 
            'Histogram' : make_float(macd - signal)
        }
    except:
        return None

def averages(x):
    return {
        '5d' : moving_average(x, 5),
        '10d' : moving_average(x, 10),
        '50d' : moving_average(x, 50),
        '200d' : moving_average(x, 200),
        'convergence' : moving_average_convergence(x)
    }
