# https://www.acmicpc.net/problem/1978

def primenumber(x):
    if x==1:
        return False
    for i in range(2, int(x ** (1 / 2) + 1)):
        if x % i == 0:
            return False
    return True




Cases = int(input())
nums = list(map(int, input().split()))
print( sum([primenumber(x) for x in nums]) )

