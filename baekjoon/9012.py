# https://www.acmicpc.net/problem/9012

import sys
n=int(sys.stdin.readline())
for i in range(n):
    s=sys.stdin.readline().rstrip()
    for i in range(50):
        s=s.replace("()", "")
        if s=="":
            break
    print("YES" if s=="" else "NO")
