# https://www.acmicpc.net/problem/10799
'''
1. 아이디어 :
- ()를 0으로 대체한다.
- for문을 돌면서 '0'을 만나면 stack의 길이만큼 더하고,'('를 만나면 stack에 넣고, ')'를 만나면 stack에서 pop하면서 1을 더한다.

2. 시간복잡도 :
- O(n*(m1 + m2/m1)) + O(n) * O(1) * O(1) = O(n*(m1 + m2/m1)) + O(n) = O(n*(m1 + m2/m1)) = O(n * (2 + 1/2)) = O(n * 2.5) = O(n)
- n : 입력받은 문자열의 길이, m1 : 대체되는 str길이, m2 : 대체되는 str의 길이

3. 자료구조 :
- 스택.
'''
import sys
s = sys.stdin.readline().strip().replace("()", "0")
ans = 0
alist = []
for char in s:
    if char == "0":
        ans+=len(alist)
    elif char == "(":
        alist.append(1)
    elif char == ")":
        ans+=1
        alist.pop()
print(ans)