#https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    if len(s)%2==1:
        return (s[int(len(s)/2-0.5)])
    else:
        return (s[int(len(s)/2-1):int(len(s)/2-1)+2])