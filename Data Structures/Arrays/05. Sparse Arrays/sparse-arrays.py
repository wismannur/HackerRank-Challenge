#!/bin/python3
# sumber link test https://www.hackerrank.com/challenges/sparse-arrays/problem

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):

    # short solutions
    return [strings.count(word) for word in queries]

    # long solutions
#     data = []
#     for isi in range(len(queries)) :
#         # print(isi)
#         data.append(0)
#         # print(data[isi])
#         for item in range(len(strings)) :
#             if queries[isi] == strings[item] :
#                 data[isi] = data[isi] + 1
    
#     return data
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
