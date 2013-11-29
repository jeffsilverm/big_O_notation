#! /usr/bin/env python
#
# This program is an implementation of an recursive binary search
#
import bisect


# Algorithm from http://rosettacode.org/wiki/Binary_search#Python
def library_binary_search(corpus, value_sought, low = 0, high = -1):
    return bisect.bisect_left(corpus, value_sought) # leftmost insertion point

if "__main__" == __name__ :
    import time_searches   # We need this to create the corpus and value_sought

    value_sought = time_searches.corpus[time_searches.value_sought_idx]
    print "The value sought is %s" % value_sought
    print "The size of the corpus is %d" % len ( time_searches.corpus )
   
    answer_idx = library_binary_search(time_searches.corpus, value_sought)

    print "The answer is at %d and is %s" % ( answer_idx,
                                              time_searches.corpus[answer_idx] )
    print "The correct answer is %d" % time_searches.value_sought_idx
