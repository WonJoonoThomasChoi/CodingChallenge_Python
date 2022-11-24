#https://school.programmers.co.kr/learn/courses/30/lessons/131705

def solution(number):
    count=0
    for a in range(len(number)-2):
        for b in range(a+1,len(number)-1):
            for c in range(b+1,len(number)):
                if number[a]+number[b]+number[c]==0:
                    print(number[a],number[b],number[c])
                    count+=1
    return count