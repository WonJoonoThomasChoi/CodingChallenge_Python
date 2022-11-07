# https://www.codewars.com/kata/5571f712ddf00b54420000ee

def loose_change(cents):
    print(cents)
    ans={}
    ans["Nickels"]=1
    print(ans["Nickels"])
    q,d,p,n=0,0,0,0
    while cents>=25:
        cents-=25
        q+=1
    while cents>=10:
        cents-=10
        d+=1
    while cents>=5:
        cents-=5
        n+=1
    while cents>=1:
        cents-=1
        p+=1
    print(q,d,n,p)
    ans["Nickels"]=n
    ans["Pennies"]=p
    ans["Dimes"]=d
    ans["Quarters"]=q
    return ans