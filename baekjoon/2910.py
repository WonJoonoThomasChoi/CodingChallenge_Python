# https://www.acmicpc.net/problem/2910
'''
1. 아이디어 :
    1) 딕셔너리를 이용하여 빈도수를 추적한다.
2. 시간복잡도 :
    1) O(n) + O(nlogn) + O(n) = O(nlogn)
    - n개의 원소를 입력받고 + n개의 원소를 정렬하고 + n개의 원소를 출력한다.
3. 자료구조 :
    1) 딕셔너리
'''
import sys
n, c = map(int, sys.stdin.readline().split())
alist = list(map(int, sys.stdin.readline().split()))
adict = {}
for i in alist:
    adict[i] = 1 if i not in adict else adict[i] + 1

alist = sorted(adict, key=lambda x: adict[x], reverse=True)
for i in alist:
    print((str(i)+" ")*adict[i], end="")
