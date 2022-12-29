# https://www.acmicpc.net/problem/1712
'''
2 8 20 38
 6 12 18
'''
n = int(input())
alist = [1]
temp=alist[0]
count=1
while temp<n:
    temp=alist[-1]+(6*count)
    alist.append(temp)
    count+=1
print(len(alist))