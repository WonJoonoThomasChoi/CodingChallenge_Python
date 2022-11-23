#https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    ans=""
    for i in s:
        if ord(i) in range(97,123):
            ans+=chr(((ord(i)-97+n)%26)+97)
        elif ord(i) in range(65,91):
            ans+=chr(((ord(i)-65+n)%26)+65)
        else:
            ans+=" "
    print(ans)
    return ans