# https://www.acmicpc.net/problem/16968

import sys
s = sys.stdin.readline().rstrip()
result = 1
for i in range(len(s)):
    if s[i] == 'd':
        if i == 0:
            result *= 10
        else:
            if s[i-1] == 'd':
                result *= 9
            else:
                result *= 10
    else:
        if i == 0:
            result *= 26
        else:
            if s[i-1] == 'c':
                result *= 25
            else:
                result *= 26
print(result)
