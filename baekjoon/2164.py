# https://www.acmicpc.net/problem/2164

'''
1. 아이디어 :
    1) 큐를 이용한다.
2. 시간복잡도 :
    1) O(n)
    - n개의 원소를 append(1)와 pop(1)
3. 자료구조 :
    1) 큐
'''
import sys
from collections import deque
n = int(sys.stdin.readline())
alist=deque(range(1,n+1))
for i in range(n-1):
    alist.popleft()
    alist.append(alist.popleft())
print(alist[0])