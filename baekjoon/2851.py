# https://www.acmicpc.net/problem/2851

import sys
ans=0
input = 0
alist=[]
for i in range(10):
    alist.append(int(sys.stdin.readline()))
i=0
if sum(alist)<=100:
    print( sum(alist))
else:
    while ans+input<=100:
        ans+=input
        input = alist[i]
        i+=1
    last_input = input
    last_ans = ans+last_input
    if abs(last_ans-100)>abs(ans-100):
        print(ans)
    else:
        print(last_ans)
