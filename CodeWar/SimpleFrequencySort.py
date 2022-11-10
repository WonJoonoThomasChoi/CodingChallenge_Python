# https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc

def solve(arr):
    ans=[]
    adict={}
    for i in range(len(arr)):
        if arr[i] in adict:
            adict[arr[i]]+=1
        else:
            adict[arr[i]]=1
    max=len(arr)
    alist=sorted(adict)
    while len(alist)>0:
        maxn=alist[0]
        maxc=adict[alist[0]]
        for i in range(len(alist)):
            if adict[alist[i]]>maxc:
                maxn=alist[i]
                maxc=adict[alist[i]]
        for i in range(maxc):
            ans.append(maxn)
        alist.remove(maxn)
    return ans