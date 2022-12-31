# https://www.acmicpc.net/problem/10870

import sys


def fib(n):
    return fib(n-2) + fib(n-1) if n>1 else n

print(fib(int(sys.stdin.readline())))