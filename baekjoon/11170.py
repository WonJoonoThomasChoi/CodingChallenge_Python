# https://www.acmicpc.net/problem/11170

def check(n):
    count=0
    for i in str(n):
        if i=="0":
            count+=1
    return count

import sys
cases = int(sys.stdin.readline())
for _ in range(cases):
    n,m = map(int,sys.stdin.readline().split())
    count=0
    for i in range(n,m+1):
        count+=check(i)
    print(count)