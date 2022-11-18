#https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6

def sum_arrays(array1,array2):
    num1=""
    num2=""
    if array1==[] and array2==[]:
        return []
    if array1!=[]:
        for i in array1:
            num1+=str(i)
        num1=int(num1)
    else:
        num1=0
    if array2!=[]:
        for i in array2:
            num2+=str(i)
        num2=int(num2)
    else:
        num2=0
    ans=[]
    if (num1+num2)>=0:
        for i in str(num1+num2):
            ans.append(int(i))
    else:
        for i in str(num1+num2)[1:]:
            ans.append(int(i))
        ans[0]=ans[0]*-1
    return ans