# https://www.acmicpc.net/problem/11557

import sys
cases = int(sys.stdin.readline())

for i in range(cases):
    school_list = []
    for i in range(int(sys.stdin.readline())):
        temp = sys.stdin.readline().split()
        school_list.append( [temp[0], int(temp[1])] )
    school_list.sort(key=lambda x: x[1], reverse=True)
    print(school_list[0][0])