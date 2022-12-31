# https://www.acmicpc.net/problem/2231
import sys
def method(n):
    for i in range(n):
        if i + (sum([int(x) for x in str(i)])) == n:
            return i
    return 0

print(method( int(sys.stdin.readline())))

