#https://www.acmicpc.net/problem/2581

def primenumber(x):
    if x==1:
        return False
    for i in range(2, int(x ** (1 / 2) + 1)):
        if x % i == 0:
            return False
    return True

minInput = int(input())
maxInput = int(input())
total = 0
cmin = float('inf')
for i in range(maxInput,minInput-1,-1):
    if primenumber(i):
        cmin = i
        total += i
print(total,cmin) if total else print(-1)