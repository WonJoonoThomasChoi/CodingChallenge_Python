# https://school.programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    ans=[]
    for i in range(1,n+1):
        ans.append(x*i)
    return ans