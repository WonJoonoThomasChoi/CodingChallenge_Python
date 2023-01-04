# https://www.acmicpc.net/problem/14425

import sys
n ,m = map(int, sys.stdin.readline().split())
base = set()
for _ in range(n):
    base.add(sys.stdin.readline().strip())
count = 0
for _ in range(m):
    if sys.stdin.readline().strip() in base:
        count += 1
print(count)