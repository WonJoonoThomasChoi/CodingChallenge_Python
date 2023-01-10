# https://www.acmicpc.net/problem/25325
'''
1. 아이디어 :
    1) 딕셔너리를 이용하여 인덱스를 하나씩 올린 후, sort한다
2. 시간복잡도 :
    1) O(n) + O(n) * O(n) + O(nlogn)= O(n^2)
    - for문으로 n개의 원소의 값을 0으로 초기화 + for문x2 로 인덱스값 하나씩 증가 + 정렬
3. 자료구조 :
    1) 스택
'''
import sys
n, alist = int(sys.stdin.readline()), list(sys.stdin.readline().split())
adict = {}
for i in alist:
    adict[i] = 0

for i in range(n):
    for j in list(sys.stdin.readline().split()):
        adict[j] += 1
alist = sorted(adict, key=lambda x: adict[x], reverse=True)
for i in alist:
    print(i, adict[i])