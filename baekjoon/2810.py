# https://www.acmicpc.net/problem/2810

import sys
n=int(sys.stdin.readline())
s=sys.stdin.readline().rstrip().replace("S","*S").replace("LL","*LL")
print(min(n,s.count("*")+1))
