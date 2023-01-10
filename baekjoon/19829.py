# https://www.acmicpc.net/problem/19829

'''
1. 아이디어 :
    1) 두 포인터로, lp=0, rp=0로 지정한 후, rp와 rp+1이 같다면, rp-lp+1로 max를 갱신해주고, rp+1에 lp와 rp를 둔다.
2. 시간복잡도 :
    1) O(n)
3. 자료구조 :
    1) 배열
'''

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
nums = list(map(int, input().split()))
if n==1:
    print(1)
    exit()
lp, rp = 0, 0
cmax = 1
while True:
    if nums[rp]==nums[rp+1]:
        cmax = max(cmax, rp-lp+1)
        rp+=1
        lp=rp
    else:
        rp+=1
    if rp==len(nums)-1:
        cmax = max(cmax, rp-lp+1)
        break
print(cmax)


