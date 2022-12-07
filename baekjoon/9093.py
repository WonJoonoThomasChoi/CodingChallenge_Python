#https://www.acmicpc.net/problem/9093

import sys
n = int(sys.stdin.readline())
for i in range(n):
    alist = sys.stdin.readline().replace("\n","").split(" ")
    for i in range(len(alist)):
        alist[i]=alist[i][::-1]
    print(" ".join(alist))
