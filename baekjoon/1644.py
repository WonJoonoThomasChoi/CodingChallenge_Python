# https://www.acmicpc.net/problem/1644
import sys


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


n = int(sys.stdin.readline())
if n == 1:
    print(0)
    sys.exit(0)
alist = prime_list(2, n + 1)
lp, rp, count = 0, 1, 0
total = alist[0]

while rp < len(alist) + 1:
    if total == n:
        count += 1
        total -= alist[lp]
        lp += 1
    elif total > n:
        total -= alist[lp]
        lp += 1
    elif total < n:
        try:
            total += alist[rp]
        except:
            pass
        rp += 1
print(count)
