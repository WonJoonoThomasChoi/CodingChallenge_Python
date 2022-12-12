# https://www.acmicpc.net/problem/10828

import sys
import heapq
n = int(sys.stdin.readline())
heap = []
for j in range(n):
    temp = int(sys.stdin.readline().replace("\n", ""))
    if temp != 0:
        heapq.heappush(heap, -temp)
    else:
        print(0) if len(heap) == 0 else print(-heap[0])
        try:
            heapq.heappop(heap)
        except:
            continue
