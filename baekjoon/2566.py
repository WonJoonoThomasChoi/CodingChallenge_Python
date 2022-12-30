# https://www.acmicpc.net/problem/2566
import sys
ans = -1
for i in range(9):
    temp_list = list(map(int, sys.stdin.readline().split()))
    cmax = max(temp_list)
    if cmax>ans:
        ans=cmax
        index = (i, temp_list.index(cmax))
print(ans)
print(index[0]+1,index[1]+1)



