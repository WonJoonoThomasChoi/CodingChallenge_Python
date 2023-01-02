# https://www.acmicpc.net/problem/10448
import sys

def check(target,alist):
    for i in alist:
        for j in alist:
            for k in alist:
                if i+j+k==target:
                    return 1
    return 0


alist=[]
for i in range(1,100):
    if i*(i+1)/2>1000:
        break
    alist.append(i*(i+1)/2)

for i in range(int(sys.stdin.readline())):
    print(check(int(sys.stdin.readline()),alist))


