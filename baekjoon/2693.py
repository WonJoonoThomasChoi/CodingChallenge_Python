# https://www.acmicpc.net/problem/2693

import sys
for i in range(int(sys.stdin.readline())):
    alist = list(map(int, sys.stdin.readline().split()))
    alist.sort()
    print(alist[-3])