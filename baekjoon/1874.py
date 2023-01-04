# https://www.acmicpc.net/problem/1874

import sys

n,  alist, pointer, ans = int(sys.stdin.readline()), [0], 1, ""
for i in range(n):
    temp = int(sys.stdin.readline())
    if temp < alist[-1]:
        print("NO")
        break
    while alist[-1] != temp:
        alist.append(pointer)
        pointer += 1
        ans += "+"
    alist.pop()
    ans += "-"
else:
    for i in ans:
        print(i)