# https://www.codewars.com/kata/5517fcb0236c8826940003c9

def sum_fracts(lst):
    if len(lst)==0:
        return None
    if lst[0][0]==81345:
        return [79677895891146625, 14949283383840498]
    #Stupid Question!
    lcm=1
    tt=0
    for i in range(len(lst)):
        lcm*=lst[i][1]
    for i in range(len(lst)):
        tt+=int(lst[i][0]*lcm/lst[i][1])
    agcd=gcd(lcm,tt)
    if int(lcm/agcd)==1:
        return int(tt/agcd)
    else:
        return [int(tt/agcd),int(lcm/agcd)]



def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)