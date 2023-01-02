#https://www.acmicpc.net/problem/24416

import sys
count={"count":0}
memo={}
def fib(n):
    if n==1 or n==2:
        count["count"]+=1
        return 1
    if n in memo:
        return memo[n]
    else:
        memo[n]=fib(n-1)+fib(n-2)
        return memo[n]

n = int(sys.stdin.readline())
fib(n)
print(fib(n), n-2)
