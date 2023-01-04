# https://www.acmicpc.net/problem/1654

import sys
k, n = map(int, sys.stdin.readline().split())
alist = [int(sys.stdin.readline()) for _ in range(k)]

def check(length):
    count=0
    for i in alist:
        count += i//length
    return count

start = 1
end = max(alist)
while start <= end:
    mid = (start+end)//2
    if check(mid) >= n:
        start = mid+1
    else:
        end = mid-1
print(end)
