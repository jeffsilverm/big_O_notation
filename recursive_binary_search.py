#! /usr/bin/env python
#
# This program is an implementation of an recursive binary search
#

# Algorithm from http://rosettacode.org/wiki/Binary_search#Python
def recursive_binary_search(corpus, value_sought, low = 0, high = -1):
    if not corpus: return -1
    if(high == -1): high = len(corpus)-1
    if low == high:
        if corpus[low] == value_sought: return low
        else: return -1
    mid = (low+high)//2
    if corpus[mid] > value_sought: return recursive_binary_search(corpus,
                                                    value_sought, low, mid-1)
    elif corpus[mid] < value_sought: return recursive_binary_search(corpus,
                                                    value_sought, mid+1, high)
    else: return mid

if "__main__" == __name__ :
    import time_searches   # We need this to create the corpus and value_sought
    sys.setrecursionlimit(15000)    # run this on a 64 bit machine - we go deep

    value_sought = time_searches.corpus[time_searches.value_sought_idx]
    print "The value sought is %s" % value_sought
    print "The size of the corpus is %d" % len ( time_searches.corpus )
   
    answer_idx = recursive_binary_search(time_searches.corpus, value_sought)

    print "The answer is at %d and is %s" % ( answer_idx,
                                              time_searches.corpus[answer_idx] )
    print "The correct answer is %d" % time_searches.value_sought_idx
