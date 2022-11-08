# https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f

def compute_sum(n):
    ans=0
    for i in range(n+1):
        ans+=digitSum(i)
    return ans


def digitSum(n):
    ans=0
    for i in str(n):
        ans+=int(i)
    return ans