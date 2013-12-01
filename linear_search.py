#! /usr/bin/env python
#
#
# This program times various search algorithms
# N, where N is the size of a list of strings to be searched.  The key to the
# corpus is the position of the value to be searched for in the list.
# N is passed as an argument on the command line.

def linear_search(corpus, value_sought) :
    """This function searches through corpus, looking for a value that matches
value_sought"""
    for i in range(len(corpus)):
        if corpus[i] == value_sought :
            break
    else :
        return -1
    return i



if "__main__" == __name__ :
    import time_linear_searches    # We need this to create the corpus and value_sought
    import sys
    value_sought = ""
    value_sought_idx = -1
    
    N = int(sys.argv[1])
    time_linear_searches.create_corpus(N)

    
    value_sought = time_linear_searches.corpus[ \
                        time_linear_searches.value_sought_idx]
    print "The value sought is %s" % value_sought
    print "The size of the corpus is %d" % len ( time_linear_searches.corpus )
    
    answer_idx = linear_search(time_linear_searches.corpus, value_sought)

    print "The answer is at %d and is %s" % ( answer_idx,
                           time_linear_searches.corpus[answer_idx] )
    print "The correct answer is %d" % time_linear_searches.value_sought_idx
