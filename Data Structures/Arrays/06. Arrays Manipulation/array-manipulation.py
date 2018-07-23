#!/bin/python3
# sumber link test https://www.hackerrank.com/challenges/crush/problem

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    resultArray = []
    for i in range(n) :
        resultArray.append(0)
    
    for i in range(m) :
        a = queries[i][0] - 1
        b = queries[i][1] - 1
        k = queries[i][2]
        # print(a)
        for item in range(a, b + 1) :
            resultArray[item] = resultArray[item] + k
    
    
    return max(resultArray)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
