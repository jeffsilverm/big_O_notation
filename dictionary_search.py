#! /usr/bin/env python
#
# This program is an implementation of a dictionary search.  Dictionaries in
# python are implemented as hashing functions
#
import time_searches     # to get function random_string
import sys
import random


corpus = dict()
value_sought = ""
answer_idx=-1

def dictionary_search(corpus, value_sought):
    return corpus[value_sought]

def call_dictionary_search():
    global corpus, value_sought, answer_idx
    value_sought_idx=random.randint(0,N-1)
    value_sought = values_list[value_sought_idx]
    answer_idx = dictionary_search(corpus, value_sought)
    

def create_corpus(length):
    global corpus, value_sought, values_list
    values_list = []        # to allow to pick a value at random
    for i in range(length):
        key = time_searches.random_string(6)
        corpus[key]= i   # find the index
        values_list.append(key)



N = int(sys.argv[1])
create_corpus(N)

if "__main__" == __name__ :
    import timeit
    number = 1000    # number of repetitions
    tq = '"""'

    print "The size of the corpus is %d" % len ( corpus )
   
#    print "The answer is at %d and is %s" % ( answer_idx,
#                                              corpus[answer_idx] )
#    print "The correct answer is %d" % value_sought_idx

# This is a little pythonic trickery.  The input to the timeit.timeit method is
# a snippet of code, which gets executed number of times.  In order to
# parameterize the code, use string substitution, the % operator, to modify the
# string.  Note that this code has to import itself in order to get the
# subroutines in scope.
    iterative_call_str = "dictionary_search.call_dictionary_search()" 
    iterative_time = timeit.timeit(iterative_call_str, \
                            setup="import dictionary_search", number=number)
    print "Iterative binary search: %.2e" % iterative_time

