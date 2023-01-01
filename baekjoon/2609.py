# https://www.acmicpc.net/submit/2609
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return (a*b)/ gcd(a,b)
import sys
n, m = list(map(int,sys.stdin.readline().split()))
print(gcd(n,m))
print(int(lcm(n,m)))