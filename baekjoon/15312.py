# https://www.acmicpc.net/problem/15312

import sys

al = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
him = sys.stdin.readline().rstrip()
her = sys.stdin.readline().rstrip()
alist = [0] * (len(him) + len(her))
for i in range(len(him)):
    alist[i * 2]       = al[ord(him[i])-65]
    alist[(i * 2) + 1] = al[ord(her[i])-65]

for i in range(len(alist)-2):
    temp = [0] * (len(alist)-1)
    for j in range(len(temp)):
        temp[j] = (alist[j] + alist[j+1]) % 10
    alist = temp.copy()
print(str(alist[0])+str(alist[1]))