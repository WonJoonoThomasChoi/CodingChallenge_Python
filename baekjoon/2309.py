# https://www.acmicpc.net/problem/2309

import sys
heights = []
for i in range(9):
    heights.append(int(sys.stdin.readline()))
heights.sort()
total = sum(heights) - 100

candid = []
for i in heights:
    if i in candid:
        candid1=i
        candid2=total-i
        break
    else:
        candid.append(total-i)
heights.remove(candid1)
heights.remove(candid2)
for i in heights:
    print(i)

