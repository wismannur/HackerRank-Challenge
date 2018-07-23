#!/bin/python3
# sumber link test https://www.hackerrank.com/challenges/arrays-ds/problem


import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    return a[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split(' ')))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
    
    n = int(raw_input().strip())
    arr = raw_input().strip().split(' ')
    arr.reverse()
    print (" ".join(arr))