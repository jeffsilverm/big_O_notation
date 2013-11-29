#! /usr/bin/python
#
#
# From http://jeremykun.com/2012/07/18/the-fast-fourier-transform/
import cmath

def omega(p, q):
   return cmath.exp((2.0 * cmath.pi * 1j * q) / p)


def dft(signal):
    size = len(signal)
    X = [0+0j] * size
    for m in range(size):
        for k in range(size):
            X[m] += signal[k]*omega(size, -k*m)
    return X

