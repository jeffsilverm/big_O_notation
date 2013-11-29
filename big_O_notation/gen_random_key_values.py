#! /usr/bin/python
#
# This program generates a file of key/value pairs in ASCII format, one
# key/value pair to a line.  The key is a random integer in the range of
# 0-4.3billion. This output is suitable as an input to the sort command as
# in
# python gen_random_key_values.py 10000 | sort -n | fgrep 235
# The -r switch produces random keys (the default)
# the -s switch produces sequential keys.
# The values are random strings

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
    parser.add_argument("-s", "--sequential", help="make the keys sequential",
                    action="store_true")
    args = parser.parse_args()
    return (args.number, args.sequential)

def gen_random_value():
    """This function returns a random string, which does *not* contain
any whitespace or control characters"""
    length = random.randint(1,6)
    l = []
    for i in range(length):
# The range of printable ASCII characters is 33 to 126.  An exercise for the
# reader: re-write this function in Unicode
        l.append(chr(random.randint(33,126)))
    s = "".join(l)
    return s

                
            
    

if __name__ == "__main__" :
    (n, sequential) = parse_args()
    if sequential:
        for key in range(n):
            value = gen_random_value()
            print key,value
    else:
        random.seed()   # no arg means use /dev/urandom
        for i in range(n):
# Return a random integer N such that a <= N <= b.
            key = random.randint(0,4294967295)
            value = gen_random_value()
            print key,value

