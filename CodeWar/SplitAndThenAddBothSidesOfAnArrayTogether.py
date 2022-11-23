# https://www.codewars.com/kata/5946a0a64a2c5b596500019a

def split_and_add(numbers, n):
    count=0
    while len(numbers)!=1 and count!=n:
        count+=1
        numbers=splita(numbers)
        numbers=adda(numbers[0],numbers[1])
    return numbers

def splita(array):
    ans=[]
    if len(array)%2==0:
        ans.append(array[:int(len(array)/2)])
        ans.append(array[int(len(array)/2):])
    else:
        ans.append( array[: int(len(array)/2-0.5)])
        ans.append( array[int(len(array)/2-0.5):])
    return ans

def adda(array1,array2):
    ans=[]
    if len(array1)==len(array2):
        for i in range(len(array1)):
            ans.append(array1[i]+array2[i])
    else:
        ans.append(array2[0])
        for i in range(len(array1)):
            ans.append(array1[i]+array2[i+1])
    return ans