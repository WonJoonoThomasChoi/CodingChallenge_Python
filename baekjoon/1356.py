# https://www.acmicpc.net/problem/1356
import sys

txt = sys.stdin.readline().rstrip()


def multi(str):
    result = 1
    for i in str:
        result *= int(i)
    return result


for i in range(1, len(txt)):
    if multi(txt[:i]) == multi(txt[i:]):
        print("YES")
        break
else:
    print("NO")
