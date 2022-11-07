# https://www.codewars.com/kata/5276c18121e20900c0000235

def find_missing_number(n):
    n=sorted(n)
    if n==[]:
        return 1
    if n[0]!=1:
        return 1
    if n[-1]!=len(n)+1:
        return len(n)+1
    for i in range(0,len(n)-1):
        if n[i]+1!=n[i+1]:
            return n[i]+1