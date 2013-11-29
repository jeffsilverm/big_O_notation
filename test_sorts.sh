#! /bin/bash
#
# This script tests the timing of the sort routines
for i  in 10 50 100 200 500 1000 2000 5000 10000; do
  echo $i
  python time_sorts.py $i
done
