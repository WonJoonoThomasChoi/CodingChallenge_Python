# https://www.acmicpc.net/problem/9933

import sys

alist=[]
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().rstrip()
    if s==s[::-1]:
        print(len(s),s[len(s)//2])
        break
    if s not in alist:
        alist.append(s[::-1])
    else:
        print(len(s), s[len(s)//2])
        break
