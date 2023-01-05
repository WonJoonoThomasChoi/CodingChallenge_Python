# https://www.acmicpc.net/problem/1697

import sys

start, end = map(int, sys.stdin.readline().split())
teleport = start * 2
count=0
# while True:
for i in range(10):
    if start==end:
        break
    if start>end:
        count += start-end
        break


    #case 1
    c1_distance = end - (start + teleport)
    #case 2
    c2_distance = end - (start + 1)

    if c1_distance < c2_distance:
        start += teleport
    else:
        start += 1
    count+=1
    print("start: ", start, "end: ", end, "count: ", count)
print(count)
