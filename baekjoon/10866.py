# https://www.acmicpc.net/problem/10866

import sys
from collections import deque
dq = deque()
for i in range(int(sys.stdin.readline())):
    s=sys.stdin.readline().rstrip()
    if len(s.split()) == 2:
        s, num = s.split()
    if s == "push_front":
        dq.appendleft(num)
    elif s == "push_back":
        dq.append(num)
    elif s == "pop_front":
        print(-1 if len(dq) == 0 else dq.popleft())
    elif s == "pop_back":
        print(-1 if len(dq) == 0 else dq.pop())
    elif s == "size":
        print(len(dq))
    elif s == "empty":
        print(1 if len(dq) == 0 else 0)
    elif s == "front":
        print(-1 if len(dq) == 0 else dq[0])
    elif s == "back":
        print(-1 if len(dq) == 0 else dq[-1])