# https://www.acmicpc.net/problem/10814

import sys
person_list = []

for _ in range (int(sys.stdin.readline())):
    person_list.append ( sys.stdin.readline().rstrip().split())
for i in person_list:
    i[0]=int(i[0])
person_list.sort(key = lambda x: x[0])
for i in person_list:
    print(int(i[0]), i[1])
