# sumber link test https://www.hackerrank.com/challenges/maximum-element/problem

def max_find(stack_arr) :
    value_maxx = 0
    for i in range(len(stack_arr)) :
        if value_maxx < stack_arr[i] :
            value_maxx = stack_arr[i]
    
    return value_maxx
    
N = int(input())
stack = []
value_max = 0
for i in range(N) :
    long = input().split()
    querie = long[0]
    if len(long) == 2 and querie == '1' :
        isi = int(long[1])
        stack.append(isi)
        if value_max < isi :
            value_max = isi
    elif querie == '2' :
        delData = stack.pop()
        if delData > value_max  :
            value_max = delData
        else : value_max = max_find(stack)
    elif querie == '3' :
        print(value_max)
    else : 
        print('data tak sesuai.')
    


