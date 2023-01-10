# https://www.acmicpc.net/problem/17608
'''
1. 아이디어 :
    1) 배열을 이용하여 current max값 추적
2. 시간복잡도 :
    1) O(n)
    - for문을 돌면서 조건문 확인
3. 자료구조 :
    1) 배열
'''
import sys
num, cmax, ans = int(sys.stdin.readline()), 0, 0
alist =[]
for _ in range(num):
    alist.append(int(sys.stdin.readline()))
for i in range(num-1,-1,-1):
    if alist[i] > cmax:
        cmax = alist[i]
        ans +=1
print(ans)