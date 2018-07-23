#!/bin/python3
# sumber link test https://www.hackerrank.com/challenges/2d-array/problem

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # print(arr)
    sumarr = []
    for row in range(len(arr) - 2) :
        for column in range(len(arr[row]) - 2) :
            sumarr.append(arr[row][column] + arr[row][column + 1] + arr[row][column + 2] + arr[row + 1][column + 1] + arr[row + 2][column] + arr[row + 2][column + 1] + arr[row + 2][column + 2])
    
    sumarr.sort()
    # print(sumarr)    
    return max(sumarr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for arr_i in range(6):
        arr.append(list(map(int, input().rstrip().split(' '))))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()