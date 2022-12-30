# https://www.acmicpc.net/problem/2750

import sys
num_list = []
for i in range( int(sys.stdin.readline())):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()
for i in num_list:
    print(i)