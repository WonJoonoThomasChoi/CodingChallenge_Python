# https://www.acmicpc.net/problem/1929

def primenumber(x):
    if x==1:
        return False
    for i in range(2, int(x ** (1 / 2) + 1)):
        if x % i == 0:
            return False
    return True

cmin, cmax = map(int, input().split())
for i in range(cmin, cmax+1):
    if primenumber(i):
        print(i)