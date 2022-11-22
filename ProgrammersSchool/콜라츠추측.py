# https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    if num<=0:
        return -1
    if num==1:
        return 0
    count=0
    for i in range(500+1):
        i+=1
        if num%2==0:
            num=int(num/2)
        else:
            num=(num*3)+1
        if num==1:
            return i
    return -1