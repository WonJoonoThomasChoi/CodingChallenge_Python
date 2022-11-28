#https://www.codewars.com/users/724thomas2/completed_solutions

def gcdi(x,y):
    if y==0:
        return abs(x)
    else:
        return gcdi(abs(y),abs(x%y))
def lcmu(a, b):
    a=abs(a)
    b=abs(b)
    return (a*b)/gcdi(a,b)
def som(a, b):
    return a+b
def maxi(a, b):
    return max(a,b)
def mini(a, b):
    return min(a,b)
def oper_array(fct, arr, init):
    alist=[]
    alist.append(fct(arr[0],init))
    for i in range(1,len(arr)):
        alist.append(fct(arr[i],alist[-1]))
    return alist