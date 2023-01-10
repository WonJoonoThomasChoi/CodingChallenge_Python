# https://www.acmicpc.net/problem/14465

'''
1. 아이디어 :
    1) 배열에서 두 포인터로(a, a+k) 슬라이딩 윈도우를 하면서 current total = current total- [lp] + [rp]를 끝까지 하면서
    total의 최솟값을 구하면 된다.
2. 시간복잡도 :
    1) O(n) + O(n-k+1) = O(n)
    - for문 입력 + n-k+1번의 for문
3. 자료구조 :
    1) 배열
'''

import sys

input = sys.stdin.readline
n, k, b = map(int, input().split())
nums = [0] * n
for _ in range(b):
    nums[int(input()) - 1] = 1
lp, rp = 0, k
ctotal = ans = sum(nums[lp:rp])
for i in range(1, n - k + 1):
    ctotal = ctotal - nums[lp] + nums[rp]
    ans = min(ans, ctotal)
    lp += 1
    rp += 1
print(ans)
