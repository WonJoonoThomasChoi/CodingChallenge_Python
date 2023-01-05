# https://www.acmicpc.net/problem/20291

import sys
from collections import Counter
file_extensions = []
for _ in range(int(sys.stdin.readline())):
    file_extensions.append(sys.stdin.readline().split('.')[1].rstrip())
file_extensions.sort()
file_extensions = Counter(file_extensions)
for key, value in file_extensions.items():
    print(key, value)
