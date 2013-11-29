#! /usr/bin/python
#
# Test the fft and dft modules

import fft
import dft
import math

SIZE = 64
TWO_PI = 2.0*math.pi
SCALE = TWO_PI/SIZE
X = x = [0] * SIZE
for i in range(0,SIZE):
    x[i] = complex( math.cos(4.0*i*SCALE), math.cos(6.0*i*SCALE) )
    print "%d:%5.2f+%5.2fj" % ( i,x[i].real, x[i].imag )

X = fft.fft(x)
print "FFT"
for i in range(0,SIZE):
    print"%d:%5.2f+%5.2fj" % ( i,X[i].real,X[i].imag )

print "DFT"
X = dft.dft(x)
for i in range(0,SIZE):
    print "%d:%5.2f+%5.2fj" % ( i,X[i].real,X[i].imag )


        
