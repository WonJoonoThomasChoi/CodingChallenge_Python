# https://www.acmicpc.net/problem/10872

import sys

def fac(n):
    return fac(n-1) * n if n>1 else 1

print( fac (int(sys.stdin.readline())))