#! /usr/bin/env python
#
#
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
    print("Bubble Sort:", timeit.timeit("time_sorts.call_bubble_sort(%d)" % N ,
          setup="import time_sorts", number=10000))
    print("Merge Sort:", timeit.timeit("time_sorts.call_merge_sort(%d)" % N ,
          setup="import time_sorts", number=10000))
