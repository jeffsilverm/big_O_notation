#! /usr/bin/python
#
#
# From http://jeremykun.com/2012/07/18/the-fast-fourier-transform/
import cmath
# See http://docs.scipy.org/doc/numpy-1.7.0/reference/generated/numpy.fft.fft.html
from numpy.fft import fft
from numpy import array

# I think the overhead of a function call outweights the clarity gained
def omega(p, q):
   return cmath.exp((2.0 * cmath.pi * 1j * q) / p)


def dft(signal):
    """This is an implementation of the Discrete Fourier Transform.  It is not
fast, going as O(n^2).  signal is a list of complex numbers, of any length"""
    size = len(signal)
    X = [0+0j] * size
    for m in range(size):
        for k in range(size):
            X[m] += signal[k]*omega(size, -k*m)
    return X

# From http://rosettacode.org/wiki/Fast_Fourier_transform#Python
def fft(signal):
    """This is an implementation of the Fast Fourier Transform, which is an
implementation of the Discrete Fourier Transform.  It goes as O(n*log(n))
signal is a list of complex numbers, of length which is a power of two"""
    N = len(signal)
    if N <= 1:
        return signal
# An optimization not found in the rosettacode implementation
    w = -2j*cmath.pi/N

    even = fft(signal[0::2])   # Pick up even elements
    odd =  fft(signal[1::2])   # Pick up odd elements
    return [even[k] + cmath.exp(w*k)*odd[k] for k in xrange(N/2)] + \
           [even[k] - cmath.exp(w*k)*odd[k] for k in xrange(N/2)]
    

# from http://rosettacode.org/wiki/Fast_Fourier_transform#Python
def numpy_fft(signal):
    """This is an implementation of the Fast Fourier Transform, which is an
implementation of the Discrete Fourier Transform.  It goes as O(n*log(n))
signal is a list of complex numbers, of length which is a power of two.  However,
this implementation uses number, which is a highly optimized library written in
C and FORTRAN"""

#    if __name__ == "__main__" :
#        a = array((0.0, 0.924, 0.707, -0.383, -1.0, -0.383, 0.707, 0.924, 0.0,
#                   -0.924, -0.707, 0.383, 1.0, 0.383, -0.707, -0.924))
#
#        print( ' '.join("%5.3f" % abs(f) for f in fft(a)) )

# there should be a test in here that len(signal) is a power of two
    x = array(signal)
    a = fft(x)
    return list(a)


def c2(x):
    """Return True if x is a power of 2, False otherwise.  x should be an int"""
    import math
    if type(x) != type(2) :
        raise TypeError("Should be an integer")
    if x <= 0 :
        raise ValueError("Should be a positive integer")
    n = math.log(x, 2)
    i = int(n)
    return abs(n-i) < 1.0E-15


if "__main__" == __name__ :
    import sys

    def make_nice_output(r):

        print( ' '.join("%5.3f" % abs(f) for f in r ))


    if len(sys.argv) > 1 :
        N = int(sys.argv[1])
    else:
        N = 8
    if not c2(N) :
        raise ValueError("Parameter should be a power of 2, actually is %d" % N)

    if len(sys.argv) > 2 :
        f = float(sys.argv[2])
    else :
        f = 3
        
    signal = [ cmath.exp( 2j * cmath.pi * f * i / N ) for i in xrange(N) ]
    x = signal[:]   # make a working copy

    r = dft(x)
    make_nice_output( r )

    x = signal[:]   # make a working copy
    r = fft(x)
    make_nice_output( r )


    x = signal[:]   # make a working copy
    r = numpy_fft(x)
    make_nice_output( r )

