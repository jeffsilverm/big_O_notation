#! /usr/bin/env python
#
# This program times the merge sort and the bubble sort for various values of
# N, where N is the size of a list of integers to be sorted.  N is passed as
# an argument on the command line.
import bubble_sort
import merge_sort
import random
import sys

def call_bubble_sort(N) :
    testset = range(N)
    testcase = testset[:]      # Make a copy, not a reference
    random.shuffle(testcase)
    assert testcase != testset  # we've shuffled it
    bubble_sort.bubble_sort(testcase)        # sort in place
    assert testcase == testset  # we've unshuffled it back into a copy


def call_merge_sort(N) :
    testset = range(N)
    testcase = testset[:]      # Make a copy, not a reference
    random.shuffle(testcase)
    assert testcase != testset  # we've shuffled it
    testcase = merge_sort.merge_sort(testcase)
    assert testcase == testset  # we've unshuffled it back into a copy

if __name__ == '__main__':
    import timeit
    N = int(sys.argv[1])
# This is a little pythonic trickery.  The input to the timeit.timeit method is
# a snippet of code, which gets executed number of times.  In order to
# parameterize the code, use string substitution, the % operator, to modify the
# string.  Note that this code has to import itself in order to get the
# subroutines in scope.
    print("Bubble Sort:", timeit.timeit("time_sorts.call_bubble_sort(%d)" % N ,
          setup="import time_sorts", number=10000))
    print("Merge Sort:", timeit.timeit("time_sorts.call_merge_sort(%d)" % N ,
          setup="import time_sorts", number=10000))
