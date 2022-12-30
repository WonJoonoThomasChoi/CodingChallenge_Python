# https://www.acmicpc.net/problem/10773

from collections import deque
import sys
numList = deque()
for _ in range(int(sys.stdin.readline())):
    temp = int(sys.stdin.readline())
    numList.append(temp) if temp != 0 else numList.pop()
print(sum(numList))
