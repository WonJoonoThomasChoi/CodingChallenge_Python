# https://www.acmicpc.net/problem/11651

import sys

num_list = []

for _ in range (int(sys.stdin.readline())):
    num_list.append(list(map(int, sys.stdin.readline().split()))[::-1])
num_list.sort()
for i in num_list:
    print(i[1],i[0])