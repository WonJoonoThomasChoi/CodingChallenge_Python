# https://www.acmicpc.net/problem/2587

import sys
num_list = []
for _ in range(5):
    num_list.append( int(sys.stdin.readline()))
num_list.sort()
print(int(sum(num_list)/5))
print(num_list[2])