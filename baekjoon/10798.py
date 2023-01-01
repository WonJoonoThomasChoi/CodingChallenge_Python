# https://www.acmicpc.net/problem/10798

import sys
alist = []
for i in range(5):
    temp = sys.stdin.readline().rstrip()
    alist.append([x for x in temp])
ans=""
cmax = (max([len(x) for x in alist]))
for i in range(cmax):
    for j in range(len(alist)):
        try:
            ans+=alist[j][i]
        except:
            pass
print(ans)