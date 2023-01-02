# https://www.acmicpc.net/problem/12605

import sys
for _ in range(int(sys.stdin.readline())):
    print("Case #{}: {}".format(_+1, " ".join(sys.stdin.readline().split()[::-1])))