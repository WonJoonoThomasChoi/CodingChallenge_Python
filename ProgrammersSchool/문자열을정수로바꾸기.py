# https://school.programmers.co.kr/learn/courses/30/lessons/12925?language=python3

def solution(s):
    print(s[1:])
    if s[0]=="+":
        return int(s[1:])
    elif s[0]=="-":
        return -int(s[1:])
    else:
        return int(s)

