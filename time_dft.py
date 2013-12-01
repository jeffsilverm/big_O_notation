#! /usr/bin/python
#
#
import dft
if "__main__" != __name__ :
    import time_dft



def call_dft ( signal  ) :
    dft.dft ( signal )

def call_fft ( signal ) :
    dft.fft ( signal )

def call_numpy_fft ( signal ):
    dft.numpy_fft( signal )


if "__main__" == __name__ :
    import cmath
    import sys
    import timeit
    number = 100   # number of repetitions
    f = float(sys.argv[1])
    print "N\tDFT\tFFT\tnumpy_FFT"
    for N in [32, 64, 128, 256, 512, 1024, 2048 ]:
        signal = [ cmath.exp( 2j * cmath.pi * f * i / N ) for i in xrange(N) ]
        signal_string = str( signal )
# The output of the signal generator is a list.  Converting a list to a string
# representation of a list works here because the input to the timeit.Timer
# function is a snippet of code.
        t_dft = timeit.timeit("dft.dft("+signal_string+")",
                             setup="import time_dft, dft",
                             number=number)
        t_fft = timeit.timeit("time_dft.call_fft("+signal_string+")",
                             setup="import time_dft, dft",
                             number=number )
        t_numpy_fft = timeit.timeit("time_dft.call_numpy_fft("+signal_string+")",
                             setup="import time_dft, dft",
                             number=number)
        print "%d:\t%5.3f\t%5.3f\t%5.3f" % (N, t_dft, t_fft, t_numpy_fft )
        
        



           
