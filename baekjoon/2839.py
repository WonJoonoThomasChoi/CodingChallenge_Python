# https://www.acmicpc.net/problem/2839

import sys
n = int(sys.stdin.readline().replace("\n", ""))
count = 0
while n >= 0:
    if n % 5 == 0:
        count += n / 5
        n = 0
        break
    n = n - 3
    count += 1
print(int(count) if n == 0 else -1)
