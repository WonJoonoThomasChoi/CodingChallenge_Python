# https://www.acmicpc.net/problem/1934

def lcm(a,b):
    return (a*b)/ gcd(a,b)

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

import sys
for i in range(int(sys.stdin.readline())):
    a,b = list(map(int,sys.stdin.readline().split()))
    print(int(lcm(a,b)))