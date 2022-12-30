# https://www.acmicpc.net/problem/10989

import sys
num_list = [0]*10001
for _ in range(int(sys.stdin.readline())):
    num_list[int(sys.stdin.readline())] +=1
for i in range(len(num_list)):
    for j in range(num_list[i]):
        print(i)

