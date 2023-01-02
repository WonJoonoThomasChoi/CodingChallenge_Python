# https://www.acmicpc.net/problem/14696

import sys
cases = int(sys.stdin.readline())
for _ in range(cases):
    alist = list(map(int,sys.stdin.readline().split()))[1:]
    blist = list(map(int,sys.stdin.readline().split()))[1:]
    alist.sort(reverse=True)
    blist.sort(reverse=True)
    total_length = max(len(alist), len(blist))
    if alist==blist:
        print("D")
    else:
        aVal = int("".join(map(str,alist))+("0" * (total_length-len(alist))))
        bVal = int("".join(map(str,blist))+("0" * (total_length-len(blist))))
        if aVal>bVal:
            print("A")
        else:
            print("B")





