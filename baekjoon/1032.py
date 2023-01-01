# https://www.acmicpc.net/problem/1032

import sys

alist = []
for i in range(int(sys.stdin.readline())):
    alist.append(sys.stdin.readline().rstrip())
if len(alist) == 1:
    print(alist[0])
else:
    ans = ""
    base = alist[0]
    place = 0
    for i in range(len(base)):
        temp = []
        for word in alist:
            if word[i] not in temp:
                temp.append(word[i])
        if len(temp) == 1:
            ans += temp[0]
        else:
            ans += "?"
    print(ans)
