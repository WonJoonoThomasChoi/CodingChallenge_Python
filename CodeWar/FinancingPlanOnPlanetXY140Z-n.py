#https://www.codewars.com/kata/559ce00b70041bc7b600013d

def finance(n):
    ans=0
    n=n+1
    for i in range(n):
        ans+=numw(n,i)
    return ans


def numw(num,week):
    ans=0
    for i in range(num-week):
        ans+=i+(2*week)
    return ans
