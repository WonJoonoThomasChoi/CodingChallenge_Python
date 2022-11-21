# https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004

def highest_rank(arr):
    adict={}
    for i in arr:
        if i not in adict:
            adict[i]=1
        else:
            adict[i]=adict[i]+1
    max=0
    ans=0
    for i in adict:
        if adict[i]>max:
            print(i,adict[i])
            max=adict[i]
            ans=i
        elif adict[i]==max:
            if i>ans:
                ans=i
    return ans