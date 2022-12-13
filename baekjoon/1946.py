# https://www.acmicpc.net/problem/1946

import sys

case = int(sys.stdin.readline())
ans=[]
for j in range(case):
    alist=[]
    n= int(sys.stdin.readline())
    for i in range(n):
        alist.append(list( map(int, sys.stdin.readline().replace("\n","").split(" "))))
    alist.sort(key = lambda x: x[0])
    count=1
    standard=alist[0][1]
    for i in range(1,n):
        if standard>alist[i][1]:
            count+=1
            standard=alist[i][1]
    print(count)


#
# 3 6
# 7 3
# 4 2
# 1 4
# 5 7
# 2 5
# 6 1
#
# 1 4 v
# 2 5
# 3 6
# 4 2 v
# 5 7
# 6 1 v
# 7 3 v
#
# 6 1
# 4 2
# 7 3
# 1 4


