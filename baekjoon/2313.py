# TODO: working on it
# https://www.acmicpc.net/problem/2313


alist1 = [30, 70, -10, 10, 0]
alist2 = [90, 80, 70, 60, 0, -60, 0, 60, -60]
alist3 = [0, 0, 0, 10, 0]
alist4 = [2, 3, -10, 5]
alist5 = [3, 5, -8, 5, 3]
alist6 = [5, 3, -8, 3, 5]
alist7 = [-20, -10, -10, -10, -10]
alist8 = [5, -10, 2, 3]
# print(res)

import sys
case = int(sys.stdin.readline())
total = 0
coords = []
for i in range(case):
    count = int(sys.stdin.readline())
    temp = list(map(int, input().split()))
    cmax = -float('inf')
    clp = 0
    crp = 1
    lp = 0
    rp = 1
    while lp <= len(temp) and rp <= len(temp):
        tempSum = sum(temp[lp:rp])
        if tempSum > 0:
            if tempSum > cmax:
                cmax = tempSum
                clp = lp
                crp = rp
            elif tempSum == cmax:
                if rp - lp < crp - clp:
                    clp = lp
                    crp = rp
                elif rp - lp == crp - clp:
                    new = int("".join([str(i) for i in temp[lp:rp]]))
                    cur = int("".join([str(i) for i in temp[clp:crp]]))
                    if new < cur:
                        clp = lp
                        crp = rp
            rp += 1
        else:
            lp += 1
            rp = lp + 1
    if cmax != -float('inf'):
        total += cmax
        coords.append([clp + 1, crp])
    else:
        total += max(temp)
        clp = temp.index(max(temp))
        crp = clp + 1
        coords.append([clp + 1, crp])
print(total)
for i in range(len(coords)):
    print(coords[i][0], coords[i][1])
