# https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8

def remove_parentheses(s):
    while "(" in s:
        maxSIndex=0
        maxEIndex=0
        for i in range(len(s)):
            if s[i]=="(":
                maxSIndex=i
        temp=s[maxSIndex::]
        for i in range(len(temp)):
            if temp[i]==")":
                maxEIndex=maxSIndex+i
                break
        s=s[:maxSIndex]+s[maxEIndex+1::]
        print(s)
    return s