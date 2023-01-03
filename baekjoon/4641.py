# https://www.acmicpc.net/problem/4641

import sys
alist=[]

while True:
    count=0
    uInput =sys.stdin.readline().rstrip()
    if uInput == "-1":
        break
    alist = list(map(int, uInput.split()))[:-1]
    alist.sort()
    for i in alist:
        if i*2 in alist:
            count+=1
    print(count)
