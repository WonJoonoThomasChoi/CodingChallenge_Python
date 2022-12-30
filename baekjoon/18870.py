# https://www.acmicpc.net/problem/18870

import sys
input()
num_list = list(map(int, sys.stdin.readline().split()))
num_list2 = sorted(list(set(num_list)))
num_dict = {num_list2[i] : i for i in range(len(num_list2))}
for i in num_list:
    print(num_dict[i], end = ' ')