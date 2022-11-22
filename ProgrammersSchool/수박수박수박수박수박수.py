#https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    str=""
    while n>1:
        str+="수박"
        n-=2
    return str if n==0 else str+"수"