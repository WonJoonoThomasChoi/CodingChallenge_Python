# https://www.acmicpc.net/problem/19947

import sys
h, y = map(int, sys.stdin.readline().split())
cmax = 0
alist=[]
def invest(money, year):
    global cmax
    if year<=0:
        cmax = max(cmax, money)
        return
    if year>=1:
        invest(int(money*1.05), year-1)
    if year>=3:
        invest(int(money*1.2), year-3)
    if year>=5:
        invest(int(money*1.35), year-5)
invest(h, y)
print(cmax)

