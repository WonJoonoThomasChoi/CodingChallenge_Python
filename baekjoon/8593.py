# https://www.acmicpc.net/problem/8595

import sys
input()
s=sys.stdin.readline().rstrip()
alist=[]
temp="0"
for i in s:
    if i.isalpha():
        alist.append(int(temp))
        temp="0"
    else:
        temp+=i
alist.append(int(temp))
print(sum(alist))