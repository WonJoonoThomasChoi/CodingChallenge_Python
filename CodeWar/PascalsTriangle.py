#https://www.codewars.com/kata/52945ce49bb38560fe0001d9

def pascal(p):
    if p==1:
        return [[1]]
    elif p==2:
        return [[1],[1,1]]
    alist=[[1],[1,1]]
    temp=[1,1]
    for j in range(p-2):
        temp2=[]
        temp2.append(1)
        for i in range(len(temp)-1):
            temp2.append(temp[i]+temp[i+1])
        temp2.append(1)
        alist.append(temp2)
        temp=temp2.copy()
    return alist