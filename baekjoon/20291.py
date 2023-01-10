# https://www.acmicpc.net/problem/20291
'''
1. 아이디어 :
    1) "."기준으로 split()후 인덱스1의 입력값을 배열에 넣고, Counter함수를 이용하여 갯수 확인
2. 시간복잡도 :
    1) O(n) + O(nlogn) + O(n) = O(nlogn)
    - n개 입력(1) + n개 정렬(logn) + n개 출력(1)
3. 자료구조 :
    1) 배열
'''
import sys
from collections import Counter
file_extensions = []
for _ in range(int(sys.stdin.readline())):
    file_extensions.append(sys.stdin.readline().split('.')[1].rstrip())
file_extensions.sort()
file_extensions = Counter(file_extensions)
for key, value in file_extensions.items():
    print(key, value)
