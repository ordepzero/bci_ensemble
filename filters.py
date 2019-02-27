# -*- coding: utf-8 -*-
from scipy import signal

def chebyshev1_filter(signals,lowcut, highcut, order):

  
    b, a = signal.cheby1(order, 0.1,[lowcut, highcut],'bandpass')
    
    filtered_signals = []
    for i in range(len(signals)):
        temp = signal.decimate(signals[i],12)
        filtered_signals.append(signal.lfilter(b, a, temp))
        

    return filtered_signals 