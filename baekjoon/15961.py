# https://www.acmicpc.net/problem/15961

import sys
from collections import defaultdict

n, d, k, c = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.extend(nums[:k - 1])
adict = defaultdict(int)
adict[c] = 1
for i in range(k):
    if nums[i] in adict:
        adict[nums[i]] += 1
    else:
        adict[nums[i]] = 1
cmax = len(adict)

for i in range(0, n - 1):
    adict[nums[i]] -= 1
    adict[nums[i + k]] += 1
    if adict[nums[i]] == 0:
        del adict[nums[i]]
    cmax = max(cmax, len(adict))
print(cmax)
