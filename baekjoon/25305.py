# https://www.acmicpc.net/problem/25305

import sys
n = int(sys.stdin.readline().split()[1])
print( sorted(list(map(int,sys.stdin.readline().split())))[-n] )