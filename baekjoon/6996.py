# https://www.acmicpc.net/problem/6996

import sys
n=int(sys.stdin.readline())
for i in range(n):
    alist = list(map(str,sys.stdin.readline().rstrip().split()))
    if sorted(alist[0]) == sorted(alist[1]):
        print("{} & {} are anagrams.".format(alist[0],alist[1]))
    else:
        print("{} & {} are NOT anagrams.".format(alist[0],alist[1]))