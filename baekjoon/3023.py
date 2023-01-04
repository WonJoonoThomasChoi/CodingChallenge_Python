# https://www.acmicpc.net/problem/3023

import sys

r, c = map(int, sys.stdin.readline().split())
a = []

for i in range(r):
    temp = sys.stdin.readline().rstrip()
    a.append([x for x in (temp+temp[::-1])])

for i in range(len(a)-1,-1,-1):
    a.append(a[i].copy())


ex, ey = map(int, sys.stdin.readline().split())
a[ex-1][ey-1] = "#" if a[ex-1][ey-1] == "." else "."

for i in a:
    print("".join(i))


