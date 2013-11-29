#! /usr/bin/python
#
# This program generates a number of random integers in ASCII format, one
# integer to a line.  This output is suitable as an input to the sort command as
# in
# python gen_random_numbers.py 10000 | sort -n
# The -r switch produces random numbers (the default)
# the -s switch produces sequential numbers

import argparse
import random
import sys

def parse_args():
    """Parse the command line arguments.  Return the number of numbers desired
(specified by the -n switch, default is 10000).  If the -s switch is given,
then set the sequential flag.  If the -r switch is given, clear the sequential
flag (this is the default)"""
    parser = argparse.ArgumentParser()
    parser.add_argument("number", help="The number of numbers to generate",
                    type=int)
    parser.add_argument("-s", "--sequential", help="make the numbers sequential",
                    action="store_true")
    args = parser.parse_args()
    return (args.number, args.sequential)


if __name__ == "__main__" :
    (n, sequential) = parse_args()
    random.seed()   # no arg means use /dev/urandom
    if sequential:
        for i in range(n):
            print i
    else:
        for i in range(n):
# Return a random integer N such that a <= N <= b.
            print random.randint(-2147483648,2147483647)
