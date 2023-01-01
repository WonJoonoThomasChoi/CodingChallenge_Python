# https://www.acmicpc.net/problem/4344

import sys

for i in range(int(sys.stdin.readline())):
    alist = list(map(int,sys.stdin.readline().split()))[1:]
    average = sum(alist)/len(alist)
    count=0
    for i in alist:
        if i>average:
            count+=1
    ans = str(round(count/len(alist)*100000)/1000)
    while len(ans[ans.index("."):])!=4:
        ans+="0"
    print(ans + "%")