# https://www.acmicpc.net/problem/1526

def contains(n):
    for i in str(n):
        if i not in "47":
            return False
    return True

import sys
num = int(sys.stdin.readline())
while True:
    if contains(num):
        print(num)
        break
    else:
        num-=1
