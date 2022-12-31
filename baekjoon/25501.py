# https://www.acmicpc.net/problem/25501
import sys


def isPalindrome(str):
    return recursion(str, 0, len(str) - 1)


def recursion(str, l, r):
    ans["count"] += 1
    if l >= r:
        return 1, ans["count"]
    elif str[l] != str[r]:
        return 0, ans["count"]
    else:
        return recursion(str, l + 1, r - 1)


for _ in range(int(sys.stdin.readline())):
    ans = {"count": 0}
    temp = isPalindrome(sys.stdin.readline().rstrip())
    print(temp[0], temp[1])
