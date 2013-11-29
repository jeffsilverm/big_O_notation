#! /usr/bin/env python
#
#

import sys

if sys.hexversion < 0x02060000 :
    def merge(left, right):
        result = []
        left_idx, right_idx = 0, 0
        while left_idx < len(left) and right_idx < len(right):
# change the direction of this comparison to change the direction of the sort
            if left[left_idx] <= right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
     
        if left:   # left is true if there is something in it
            result.extend(left[left_idx:])
        if right:
            result.extend(right[right_idx:])
        return result
else :
# heapq was implemented in python 2.6
    from heapq import merge


def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) / 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    merged = list(merge(left, right))
    return merged


if __name__ == "__main__":
   """Sample usage and simple test suite"""
 
   from random import shuffle
 
   testset = range(100)
   testcase = testset[:] # make a copy
   shuffle(testcase)
   assert testcase != testset  # we've shuffled it
   testcase = merge_sort(testcase)    # Makes a new copy
   assert testcase == testset  # we've unshuffled it back into a copy
