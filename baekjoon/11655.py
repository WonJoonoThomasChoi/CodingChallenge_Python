# https://www.acmicpc.net/problem/11655

import sys

sentence = sys.stdin.readline().rstrip()
ans = ""
for letter in sentence:
    if 65 <= ord(letter) <= 90:
        ans += chr((ord(letter) - 65 + 13) % 26 + 65)
    elif 97 <= ord(letter) <= 122:
        ans += chr((ord(letter) - 97 + 13) % 26 + 97)
    else:
        ans += letter
print(ans)
