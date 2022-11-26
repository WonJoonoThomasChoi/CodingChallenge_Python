#https://www.codewars.com/kata/554e52e7232cdd05650000a0

def lowest_product(input):
    alist=[]
    if len(input)<4:
        return "Number is too small"
    else:
        for i in range(len(input)-3):
            alist.append(maxm(input[i:i+4]))
    return min(alist)
def maxm(array):
    ans=1
    for i in array:
        ans*=int(i)
    return ans