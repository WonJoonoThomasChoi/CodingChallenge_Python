# https://www.acmicpc.net/problem/10845

import sys
n = int(sys.stdin.readline())

alist=[]
for i in range(n):
    command = sys.stdin.readline().rstrip()
    if len(command.split()) == 2:
        command, num = command.split()

    if command == "push":
        alist.append(num)
    elif command == "pop":
        print(-1 if len(alist) == 0 else alist.pop(0))
    elif command == "size":
        print(len(alist))
    elif command == "empty":
        print(1 if len(alist) == 0 else 0)
    elif command == "front":
        print(-1 if len(alist) == 0 else alist[0])
    elif command == "back":
        print(-1 if len(alist) == 0 else alist[-1])
