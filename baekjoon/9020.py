# https://www.acmicpc.net/problem/9020

def prime_list(start, end):
    sieve = [True] * end
    if start <= 0:
        start = 2
    m = int(end ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, end, i):
                sieve[j] = False
    return [i for i in range(start, end) if sieve[i]]


import sys

for i in range(int(sys.stdin.readline())):
    inputNum = int(sys.stdin.readline())
    num_list = prime_list(0, inputNum)
    lp, rp = 0, len(num_list) - 1
    cmin, cmax = 0, 0
    while lp <= rp:
        if num_list[lp] + num_list[rp] == inputNum:
            cmin, cmax = num_list[lp], num_list[rp]
            lp += 1
            rp -= 1
        elif num_list[lp] + num_list[rp] >= inputNum:
            rp -= 1
        else:
            lp += 1
    print(cmin, cmax)
