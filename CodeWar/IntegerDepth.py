#https://www.codewars.com/kata/59b401e24f98a813f9000026

def compute_depth(n):
    ans=[]
    j=1
    while len(ans)!=10:
        for i in sinnum(n*j):
            if i not in ans:
                ans.append(i)
        j+=1
    return j-1

def sinnum(n):
    temp=[]
    for i in str(n):
        temp.append(i)
    return temp