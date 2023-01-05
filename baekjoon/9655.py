# https://www.acmicpc.net/problem/9655

import sys

n = int(sys.stdin.readline())

def stone(n, last):
    if n ==0:
        return last
    else:
        if n<3:
            if last == "SK":
                return stone(n-1, "CY")
            else:
                return stone(n-1, "SK")
        else:
            if last == "SK":
                return stone(n-3, "CY")
            else:
                return stone(n-3, "SK")

print(stone(n,"CY"))

