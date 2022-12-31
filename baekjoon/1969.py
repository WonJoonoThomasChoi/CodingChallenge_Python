# https://www.acmicpc.net/problem/1969

import sys

n, m = list(map(int, sys.stdin.readline().split()))
templist = []
for i in range(n):
    templist.append(sys.stdin.readline().rstrip())

ans = ""
diff = 0
for i in range(m):
    a, c, g, t = 0, 0, 0, 0
    for j in range(n):
        if templist[j][i] == "T":
            t += 1
        elif templist[j][i] == "A":
            a += 1
        elif templist[j][i] == "G":
            g += 1
        elif templist[j][i] == "C":
            c += 1
    if max(a, t, g, c) == a:
        ans += "A"
        diff += c + g + t
    elif max(a, t, g, c) == c:
        ans += "C"
        diff += a + g + t
    elif max(a, t, g, c) == g:
        ans += "G"
        diff += c + a + t
    elif max(a, t, g, c) == t:
        ans += "T"
        diff += c + g + a
print(ans)
print(diff)
