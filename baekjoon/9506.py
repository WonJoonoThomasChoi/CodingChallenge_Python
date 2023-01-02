# https://www.acmicpc.net/problem/9506

import sys
while True:
    a = int(sys.stdin.readline())
    if a==-1:
        break
    alist=[]
    for i in range(1,a):
        if a%i==0:
            alist.append(i)
    if sum(alist)==a:
        print(str(a) + " = " + " + ".join(map(str,alist)))
    else:
        print(str(a) + " is NOT perfect.")