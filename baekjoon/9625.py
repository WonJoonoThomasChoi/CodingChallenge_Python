#https://www.acmicpc.net/problem/9625

import sys
n = int(sys.stdin.readline())
adict = {}
def fib(n):
    if n in adict:
        return adict[n]
    else:
        adict[n] = n-1 if n<=2 else fib(n - 1) + fib(n - 2)
        return adict[n]
print(fib(n),fib(n+1))

a,b=1,0
for i in range(int(input())):
    a,b=b,b+a
print(a,b)