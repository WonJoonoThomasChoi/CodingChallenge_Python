# https://www.acmicpc.net/problem/1037

import sys
cases = int(sys.stdin.readline())
alist = list(map(int,sys.stdin.readline().split()))
print(min(alist)*max(alist))


