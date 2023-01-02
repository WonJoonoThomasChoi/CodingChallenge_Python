# https://www.acmicpc.net/problem/1357
import sys
def Rev(x):
    return int(str(x)[::-1])

n, m = map(int, sys.stdin.readline().split())
print(Rev(Rev(n)+Rev(m)))