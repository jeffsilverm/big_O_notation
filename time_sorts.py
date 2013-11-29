#! /usr/bin/env python
#
# This program times the merge sort and the bubble sort for various values of
# N, where N is the size of a list of integers to be sorted.  N is passed as
# an argument on the command line.
import bubble_sort
import merge_sort
import random
import sys

testset = []
testcase = []
N = -1
def call_bubble_sort() :
    global testcase

    testcase = testset[:]      # Make a copy, not a reference, because bubble
                               # sort sorts in place and we want a reproducible
                               # test case
    bubble_sort.bubble_sort(testcase)        # sort in place


def call_merge_sort() :
    global testcase
    
    testcase = testset[:]
    testcase = merge_sort.merge_sort(testcase)


def setup_vectors() :
    global testset, testcase, N
    N = int(sys.argv[1])
    testset = range(N)
    random.shuffle(testset)

# Get called at module import time, to set the the testcase and testset
setup_vectors()
assert testcase != testset  # verify that we've shuffled it


if __name__ == '__main__':
    import timeit


# This is a little pythonic trickery.  The input to the timeit.timeit method is
# a snippet of code, which gets executed number of times.  In order to
# parameterize the code, use string substitution, the % operator, to modify the
# string.  Note that this code has to import itself in order to get the
# subroutines in scope.
    bubble_sort_time = timeit.timeit("time_sorts.call_bubble_sort()",
          setup="import time_sorts", number=10000)

    print "Bubble Sort:", bubble_sort_time

    merge_sort_time = timeit.timeit("time_sorts.call_merge_sort()",
          setup="import time_sorts", number=10000)

    print "Merge Sort:", merge_sort_time
