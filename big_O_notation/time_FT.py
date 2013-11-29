#! /usr/bin/python
#
# Test the speed of the Discrete Fourier Transform (DFT) and the Fast Fourier
# Transform


# import fft
# import dft
import timeit
import math

def signal_generator(L):
    """Returns a signal in the form of a list of complex numbers.  In this case,
the signal is a real sine wave and a imaginary cosine wave"""
    x = [0+0J] * L
    for i in range(0, L):
        x[i] = complex( math.sin(2*math.pi*4.0*i/L),
            math.cos(2*math.pi*12.0*i/L) )
    return x



for L in [32, 64, 128, 256, 512, 1024, 2048 ]:
# The output of the signal generator is a list.  Converting a list to a string
# representation of a list works here because the input to the timeit.Timer
# function is a snippet of code.
    signal_string = str( signal_generator ( L ) )
    t_fft = timeit.Timer("fft.fft(x)","import fft; x="+signal_string)
    t_dft = timeit.Timer("dft.dft(x)","import dft; x="+signal_string)
    time_fft = t_fft.repeat(1,50)
    time_dft = t_dft.repeat(1,50)
    time_fft = min( time_fft )
    time_dft = min( time_dft )
    print "For length %d, the FFT took %f seconds and the DFT took %f seconds)" % (
           L, time_fft, time_dft)
