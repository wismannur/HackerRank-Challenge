# sumber link test https://www.hackerrank.com/challenges/queue-using-two-stacks/problem

s = []
N = int(input())
for i in range(N) :
    long = input().split()
    first = long[0]
    if len(long) == 2 and first == '1' :
        s.append(long[1])
    elif first == '2' :
        s.pop(0)
    elif first == '3' :
        print(s[0])
    else :
        print('data tidak sesuai.')
    