# https://www.acmicpc.net/problem/4158

import sys
while True:
    n,m = map(int,sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    anums = [int(sys.stdin.readline()) for _ in range(n)]
    bnums = [int(sys.stdin.readline()) for _ in range(m)]
    count = 0
    lp,rp=0,0
    while lp<n and rp<m:
        if anums[lp] == bnums[rp]:
            count+=1
            lp+=1
            rp+=1
        elif anums[lp] < bnums[rp]:
            lp+=1
        else:
            rp+=1
    print(count)

'''

import sys

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    anums = [int(sys.stdin.readline()) for _ in range(n)]
    bnums = [int(sys.stdin.readline()) for _ in range(m)]
    count = 0
    for i in bnums:
        start = 0
        end = n - 1
        while start <= end:
            mid = (start + end) // 2
            if anums[mid] == i:
                count += 1
                break
            elif anums[mid] > i:
                end = mid - 1
            elif anums[mid] < i:
                start = mid + 1
    print(count)


'''