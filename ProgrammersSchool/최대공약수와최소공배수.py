#https://school.programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    return [gcd(n,m),lcm(n,m)]

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

def lcm(a,b):
    return (a*b)/ gcd(a,b)

