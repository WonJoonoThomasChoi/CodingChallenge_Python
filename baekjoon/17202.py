# https://www.acmicpc.net/problem/17202

import sys


def make_num(s):
    if len(s) == 2:
        return int(s)
    else:
        ans = ""
        for i in range(len(s) - 1):
            ans += str((int(s[i]) + int(s[i + 1]))%10)
        return make_num(ans)


A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()
s = ""
for i in range(8):
    s += A[i] + B[i]
print ("%02d" % ((make_num(s)) % 100))
