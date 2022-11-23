#https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    s=s.split(" ")
    ans=[]
    for j in s:
        temp=""
        for i in range(len(j)):
            if i%2==0:
                temp+=j[i].upper()
            else:
                temp+=j[i].lower()
        ans.append(temp)
    return " ".join(ans)