#https://www.acmicpc.net/problem/10828

import sys
n = int(sys.stdin.readline())
ans = []
for j in range(n):
    i=(sys.stdin.readline().replace("\n", "").split(" "))
    if i[0] == "push":
        ans.append(int(i[1]))
    elif i[0] == "pop":
        if len(ans) == 0:
            print(-1)
        else:
            print(ans[-1])
            ans = ans[:-1]
    elif i[0]=="size":
        print(len(ans))
    elif i[0]=="empty":
        print(0 if len(ans)!=0 else 1)
    elif i[0]=="top":
        print(-1 if len(ans)==0 else ans[-1])

