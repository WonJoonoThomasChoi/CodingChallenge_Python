#https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c/train/python

def sort_by_length(arr):
    length=len(arr)
    loc=0
    ans=[]
    for j in range(length):
        max=1000
        for i in range(len(arr)):
            if len(arr[i])<max:
                max=len(arr[i])
                loc=i
        ans.append(arr[loc])
        arr.remove(arr[loc])
    return ans