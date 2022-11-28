#https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    return len([x for x in range(2,n+1) if primenumber(x)])

def primenumber(x):
    for i in range(2, int(x**(1/2)+1)):
        if x % i == 0:
            return False
    return True