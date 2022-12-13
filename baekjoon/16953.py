# https://www.acmicpc.net/problem/16953

import sys
n = sys.stdin.readline().replace("\n", "").split(" ")
def func(n, dest, count):
    if n > dest:
        return
    elif n == dest:
        return count+1
    else:
        return func(n * 2, dest, count+1) or func(int(str(n)+"1"), dest, count+1)

count=func( int(n[0]), int(n[1]), 0)
if count==None:
    print(-1)
else:
    print(count)
