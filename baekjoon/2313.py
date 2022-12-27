# TODO: working on it
# https://www.acmicpc.net/problem/2313

import sys

case = int(sys.stdin.readline())
total = 0
coords = []
for i in range(case):
    count = int(sys.stdin.readline())
    alist = list(map(int, input().split()))
    max = -100000000
    maxl = 0
    maxr = len(alist)
    lp = 0
    rp = len(alist)
    add = 0
    while lp < rp:
        try:
            if sum(alist[lp:rp]) >= max:
                max = sum(alist[lp:rp])
                maxl = lp
                maxr = rp
            if alist[lp] > alist[rp-1]:
                rp -= 1
            elif alist[lp] < alist[rp-1]:
                lp += 1
            else:
                if alist[lp] + alist[lp + 1] > alist[rp - 1] + alist[rp - 2]:
                    rp -= 1
                elif alist[lp] + alist[lp + 1] < alist[rp - 1] + alist[rp - 2]:
                    lp += 1
            # print(lp,rp)
        except:
            break

    coords.append([maxl + 1, maxr])
    total += (max)
print(total)
for i in range(case):
    print(coords[i][0], coords[i][1])
