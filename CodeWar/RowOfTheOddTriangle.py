# https://www.codewars.com/kata/5d5a7525207a674b71aa25b5

def odd_row(n):
    start=pib(n)
    alist=[]
    for i in range(n):
        alist.append(start+(2*i))
    return alist

def pib(n):
    return n*(n-1)+1
    #1 3 7 13 21