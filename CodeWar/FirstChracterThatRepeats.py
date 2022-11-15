#https://www.codewars.com/kata/54f9f4d7c41722304e000bbb

def first_dup(s):
    for i in range(len(s)):
        if s[i] in s[i+1:]:
            return s[i]