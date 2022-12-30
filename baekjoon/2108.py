# https://www.acmicpc.net/problem/2108

import sys

num_dict = {}
num_list = []
for _ in range(int(sys.stdin.readline())):
    temp_num = int(sys.stdin.readline())
    num_list.append(temp_num)
    if temp_num not in num_dict:
        num_dict[temp_num] = 1
    else:
        num_dict[temp_num] += 1
num_list.sort()
average = sum(num_list) / len(num_list)
print(-round(-average) if average < 0 else round(average))
print(num_list[len(num_list) // 2])
cmax = max([x for x in num_dict.values()])
countMax = []
for k, v in num_dict.items():
    if num_dict[k] == cmax:
        countMax.append(k)
countMax.sort()
print(countMax[0] if len(countMax) == 1 else countMax[1])
print(num_list[-1] - num_list[0])
