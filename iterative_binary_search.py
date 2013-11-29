#! /usr/bin/env python
#
# This program is an implementation of an iterative binary search
#

# Algorithm from http://rosettacode.org/wiki/Binary_search#Python


def iterative_binary_search(corpus, value_sought) :
    """Search for value_sought in corpus corpus"""
# Note that because Python is a loosely typed language, we generally don't
# care about the datatype of the corpus
    low = 0
    high = len(corpus)-1
    while low <= high: 
        mid = (low+high)//2
        if corpus[mid] > value_sought: high = mid-1
        elif corpus[mid] < value_sought: low = mid+1
        else: return mid   # Return the index where the value was found.
    return -1  # indicate value not found


if "__main__" == __name__ :
    import time_searches   # We need this to create the corpus and value_sought

    value_sought = time_searches.corpus[time_searches.value_sought_idx]
    print "The value sought is %s" % value_sought
    print "The size of the corpus is %d" % len ( time_searches.corpus )
    
    answer_idx = iterative_binary_search(time_searches.corpus, value_sought)

    print "The answer is at %d and is %s" % ( answer_idx,
                                              time_searches.corpus[answer_idx] )
    print "The correct answer is %d" % time_searches.value_sought_idx

    
