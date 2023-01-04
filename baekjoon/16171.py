# https://www.acmicpc.net/problem/16171

import sys
s=sys.stdin.readline().rstrip()
word=sys.stdin.readline().rstrip()
temp=""
for i in s:
    if i.isalpha():
        temp+=i
print(1 if word in temp else 0)