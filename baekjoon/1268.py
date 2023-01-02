# https://www.acmicpc.net/problem/1268

import sys
n = int(sys.stdin.readline())
students = []
for i in range(n):
    students.append(list(map(int, sys.stdin.readline().split())))
ans = []
for i in range(n):
    temp = []
    for j in range(5):
        for k in range(n):
            if students[i][j] == students[k][j]:
                temp.append(k)
    ans.append(len(set(temp)))
print(ans.index(max(ans)) + 1)




