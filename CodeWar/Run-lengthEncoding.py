#https://www.codewars.com/kata/546dba39fa8da224e8000467

def run_length_encoding(s):
    if s=="":
        return []
    rep=0
    cur=s[0]
    templist=[]
    ans=[]
    for i in s:
        if i == cur:
            rep+=1
        else:
            templist.append(rep)
            templist.append(cur)
            ans.append(templist)
            templist=[]
            cur=i
            rep=1
    templist.append(rep)
    templist.append(cur)
    ans.append(templist)
    templist=[]
    return ans