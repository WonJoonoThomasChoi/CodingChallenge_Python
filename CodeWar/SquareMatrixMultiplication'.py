# https://www.codewars.com/kata/5263a84ffcadb968b6000513

def matrix_mult(a, b):
    alist=[]
    l=len(a)
    for i in range(l):
        temp=[]
        for j in range(l):
            temp.append(getVal(i,j,a,b))
        alist.append(temp)
    print(alist)
    return alist

    return

def getVal(x,y,a,b):
    l=len(a)
    ans=0
    for i in range(l):
        ans+=a[x][i]*b[i][y]
    return ans