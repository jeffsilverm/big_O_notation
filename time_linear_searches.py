#! /usr/bin/env python
#
# This program times various search algorithms
# N, where N is the size of a list of strings to be sorted.  The key to the corpus
# is the position of the value to be searched for in the list.
# N is passed as an argument on the command line.
import linear_search
import random
import sys

corpus = []
value_sought_idx = -1

def random_string( length ):
    """This function returns a random ASCII string of length length"""
    s = ''
    for i in range(length ):
# Generate a random printable ASCII character.  This assumes that space is a
# printable character, if you don't like that, then use ! )
        s = s + ( chr( random.randint(ord(' '), ord('~') ) ) )
    return str( s )


def create_corpus(N):
    """This function returns a corpus to search in.  It generates a sorted list
of values which are random strings.  It then sorts the list.  Once the corpus
is created, it gets saved as a global variable so that it will persist"""
    global corpus
    global value_sought_idx
    
    for i in range(N):
        corpus.append( random_string(6))
#    corpus.sort()       # linear search does not need the corpus to be sorted
    value_sought_idx = random.randint(0,N-1)
    return 
    
    
        
    

def call_linear_search(value_sought):
    """Call the iterative version of the binary search"""
# We need to do make a subroutine call in the scope of time_searches so we can
# pass the global variable corpus.  corpus is out of scope of the actual
# binary search routine, so we have to pass it (it gets passed by reference,
# which is fast)
    linear_search.linear_search(corpus, value_sought)   
   
N = int(sys.argv[1])
create_corpus(N)

if __name__ == '__main__':
    import timeit
    number = 100  # number of iterations
    tq = '"""'    # Need to insert a triple quote into a string

    value_sought = corpus[value_sought_idx]

# This is a little pythonic trickery.  The input to the timeit.timeit method is
# a snippet of code, which gets executed number of times.  In order to
# parameterize the code, use string substitution, the % operator, to modify the
# string.  Note that this code has to import itself in order to get the
# subroutines in scope.
    linear_call_str = "time_linear_searches.call_linear_search( " + \
                            tq + value_sought + tq + ")" 
    linear_time = timeit.timeit(linear_call_str, \
                            setup="import time_linear_searches", number=number)
    print "linear search: %.2e" % linear_time


    

