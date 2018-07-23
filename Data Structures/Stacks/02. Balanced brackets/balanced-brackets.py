# sumber link test https://www.hackerrank.com/challenges/balanced-brackets/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def mathcing(sym1, sym2) :
    if sym1 == '{' and sym2 == '}':
        return True
    elif sym1 == '[' and sym2 == ']' :
        return True
    elif sym1 == '(' and sym2 == ')' :
        return True   
    else : return False

# Complete the isBalanced function below.
def isBalanced(s):
    m = s
    panjang = len(m)
    first = m[0]
    stack = []
    YES = 'YES'
    NO = 'NO'
    
    if panjang % 2 == 0 :
        if first == '}' or first == ']' or first == ')' :
                return NO
        else :
            for i in range(len(m)) :
                if m[i] == '{' or m[i] == '[' or m[i] == '(':
                    stack.append(m[i])
                else:
                    if len(stack) != 0 :
                        isi = stack.pop()
                        result = mathcing(isi, m[i])
                        if result == True :
                            continue
                        else : return NO  
                    else : 
                        return NO
                
            if len(stack) == 0 :
                return YES
            else : 
                return NO
    else :
        return NO 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
