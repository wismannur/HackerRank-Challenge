#!/bin/python3
# sumber link test https://www.hackerrank.com/challenges/array-left-rotation/problem

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    
    # print(d)
    # print(n)
    
    for number in range(d) :
        a.append(a[0])
        a.pop(0)
        hasil = a
        # if hasil == [5, 1, 2, 3, 4] :
        #     hasil = hasil
    
    result = [str(x) for x in hasil]
    print(" ".join(result))
        
        
    
    
    
    
    
