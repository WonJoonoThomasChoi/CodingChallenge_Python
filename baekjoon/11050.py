# https://www.acmicpc.net/problem/11050

from itertools import combinations
import sys
n , m = list(map(int,sys.stdin.readline().split()))
print(len((list(combinations(range(n),m)))))