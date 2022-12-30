# https://www.acmicpc.net/problem/11650

import sys

num_list = []

for _ in range (int(sys.stdin.readline())):
    num_list.append(list(map(int, sys.stdin.readline().split())))
num_list.sort()
for i in num_list:
    print(i[0],i[1])