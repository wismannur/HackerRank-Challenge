#!/bin/python3
# sumber link test https://www.hackerrank.com/challenges/dynamic-array/problem

import os
import sys

#
# Complete the dynamicArray function below.
#
def dynamicArray(n, queries):
    #
    # Write your code here.
    #
    
    lastAns = 0
    seqList = [[] for _ in range(n)]
    result = []
    
    for querie in queries :
        index = (querie[1] ^ lastAns) % n
        seq = seqList[index]
        if querie[0] == 1 :
            seq.append(querie[2])
        elif querie[0] == 2 :
            size = len(seq)
            lastAns = seq[querie[2] % size]
            print(lastAns)
            result.append(lastAns)
    
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
