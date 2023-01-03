# https://www.acmicpc.net/problem/2435

import sys

n, k = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split()))
maxsum = float('-inf')
for i in range(n - k + 1):
    maxsum = max(maxsum,sum(alist[i:i + k]))

print(maxsum)

