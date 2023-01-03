# https://www.acmicpc.net/problem/17363

import sys


def rotate(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]) - 1, -1, -1)]


row, col = map(int, sys.stdin.readline().split())
alist = []
for _ in range(row):
    alist.append(sys.stdin.readline().rstrip())

alist = rotate(alist)

for xrow in range(col):
    for xcol in range(row):

        if alist[xrow][xcol] == "-":
            alist[xrow][xcol] = "|"
        elif alist[xrow][xcol] == "|":
            alist[xrow][xcol] = "-"
        elif alist[xrow][xcol] == "/":
            alist[xrow][xcol] = "\\"
        elif alist[xrow][xcol] == "\\":
            alist[xrow][xcol] = "/"
        elif alist[xrow][xcol] == "^":
            alist[xrow][xcol] = "<"
        elif alist[xrow][xcol] == "<":
            alist[xrow][xcol] = "v"
        elif alist[xrow][xcol] == "v":
            alist[xrow][xcol] = ">"
        elif alist[xrow][xcol] == ">":
            alist[xrow][xcol] = "^"
for i in alist:
    print("".join(i))
