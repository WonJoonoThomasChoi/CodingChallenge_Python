# https://www.acmicpc.net/problem/11179

import sys
n = int(sys.stdin.readline())
print(int(bin(n)[2:][::-1],2))