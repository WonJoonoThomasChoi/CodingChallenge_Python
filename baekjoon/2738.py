# https://www.acmicpc.net/problem/2738
import sys

n, m = map(int, sys.stdin.readline().split())


matrixA = []
matrixB = []
for i in range(n):
    temp = [int(x) for x in sys.stdin.readline().replace("\n", "").split(" ")]
    matrixA.append(temp)
for i in range(n):
    temp = [int(x) for x in sys.stdin.readline().replace("\n", "").split(" ")]
    matrixB.append(temp)

for i in range(n):
    for j in range(m):
        print(matrixA[i][j] + matrixB[i][j], end=" ")
    print()