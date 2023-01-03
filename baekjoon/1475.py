# https://www.acmicpc.net/problem/1475

import sys

n = sys.stdin.readline().rstrip()

count = [0] * 10
for i in n:
    count[int(i)] += 1
count[6] = (count[6] + count[9] + 1) // 2
count[9] = 0
print(max(count))
