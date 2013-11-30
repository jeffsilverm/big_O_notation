#! /usr/bin/env python
#
# This program is an implementation of a dictionary search.  Dictionaries in
# python are implemented as hashing functions
#
import time_searches     # to get function random_string 

corpus = dict()

def dictionary_search(corpus, value_sought):
    return corpus[value_sought]

def call_dictionary_search():
    

def create_corpus(length):
    for i in range(length):
        key = time_searches.random_string(6)
        value=i
    value_sought_idx = random.randint(0,N-1)
    for i in range(value_sought_idx):
        value

N = int(sys.argv[1])
create_corpus(N)

if "__main__" == __name__ :
    import timeit

    

    value_sought = time_searches.corpus[time_searches.value_sought_idx]
    print "The value sought is %s" % value_sought
    print "The size of the corpus is %d" % len ( time_searches.corpus )
   


    print "The answer is at %d and is %s" % ( answer_idx,
                                              time_searches.corpus[answer_idx] )
    print "The correct answer is %d" % time_searches.value_sought_idx
