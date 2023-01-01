# https://www.acmicpc.net/problem/1010

import math
import sys
def num_combinations(N, M):
    #  N! / (k! * (N-M)!)
    return math.factorial(N) / (math.factorial(M) * math.factorial(N-M))

for i in range(int(sys.stdin.readline())):
    n,m = list(map(int,sys.stdin.readline().split()))
    print(int(num_combinations(m,n)))

