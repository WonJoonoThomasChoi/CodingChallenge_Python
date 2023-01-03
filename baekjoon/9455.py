# https://www.acmicpc.net/problem/9455

def rotate_matrix_90_degrees_clockwise(matrix):
    transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    return [row[::-1] for row in transposed_matrix]


import sys
cases = int(sys.stdin.readline())
for _ in range(cases):
    n, m = map(int, sys.stdin.readline().split())
    boxes = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    boxes= rotate_matrix_90_degrees_clockwise(boxes)

    count=0
    for row in boxes:
        empty=0
        for i in range(len(row)):
            if row[i]==1:
                count+=i-empty
                empty+=1
    print(count)
