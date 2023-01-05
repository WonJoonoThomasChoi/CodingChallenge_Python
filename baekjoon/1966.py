# https://www.acmicpc.net/problem/1966

import sys

cases = int(sys.stdin.readline())
for _ in range(cases):
    n, i = map(int, sys.stdin.readline().split())
    ilist = [0] * n
    ilist[i] = 1
    alist = list(map(int, sys.stdin.readline().split()))
    count = 0
    while True:
        cmax = max(alist)
        if alist[0] == cmax:
            if ilist[0] == 1:
                print(count+1)
                break
            ilist = ilist[1:]
            alist = alist[1:]
            count += 1
        else:
            ilist.append(ilist.pop(0))
            alist.append(alist.pop(0))
