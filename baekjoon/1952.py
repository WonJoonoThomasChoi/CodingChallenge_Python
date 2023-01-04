# https://www.acmicpc.net/problem/1952

import sys
m,n=map(int,sys.stdin.readline().split())
if n>=m :
    print( 2*m -2)
else:
    print( 2*n -1)
'''
1: 0 
2: 2
3: 4
4: 6
5: 8
6: 10


'''