# https://www.codewars.com/kata/528d9adf0e03778b9e00067e

def mineLocation(f):
    l=len(f)
    for i in range(l):
        for j in range(l):
            if f[i][j]==1:
                return [i,j]