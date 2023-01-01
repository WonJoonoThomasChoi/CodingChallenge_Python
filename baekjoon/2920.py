# https://www.acmicpc.net/problem/2920

import sys
alist = list(map(int,sys.stdin.readline().split()))

if alist == sorted(alist):
    print("ascending")
elif alist == sorted(alist, reverse=True):
    print("descending")
else:
    print("mixed")