# https://www.acmicpc.net/problem/1920

import sys


def binarySearch(alist, target):
    start = 0
    end = len(alist)-1
    while start <= end:
        mid = (start + end) // 2
        if alist[mid] == target:
            return 1
        elif alist[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(sys.stdin.readline())
alist = list(map(int, sys.stdin.readline().split()))
alist.sort()
m = int(sys.stdin.readline())
blist = list(map(int, sys.stdin.readline().split()))
for i in blist:
    print(binarySearch(alist, i))



