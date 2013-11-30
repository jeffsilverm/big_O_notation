#! /bin/bash
#
# This script tests the timing of the sort routines
for i  in 1000 10000 100000 200000 500000 1000000; do
  echo $i
  python time_searches.py $i
done
