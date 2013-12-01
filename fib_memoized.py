#! /usr/bin/env python
#
# This program demonstrates the use of a cache to speed up program execution
# fib_memozied is a memoized version of the fibonnaci function.  fib is the same
# code, only not memoized for comparison purposes.
def memoize(f):
    cache = {}
    def decorated_function(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = f(n)
            return cache[n]
    return decorated_function

@memoize
def fib_memoized(n):
    return n if n < 2 else fib(n-2) + fib(n-1)


def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)


if "__main__" == __name__ :
    import sys
    import timeit

    number = 100000
    print "N\tfib\tmemoizd\tspeedup"
    for n in range(2,20,2):
        t_fib = timeit.timeit("fib_memoized.fib(%d)" % n, "import fib_memoized",
                             number=number)
        t_mem = timeit.timeit("fib_memoized.fib_memoized(%d)" % n, "import fib_memoized",
                             number=number)
    


        print "%3d:\t%5.3f\t%5.3f\t%8.2f" % (n, t_fib, t_mem, t_fib/t_mem)

