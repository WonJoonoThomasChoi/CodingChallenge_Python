#https://www.codewars.com/kata/58ae6ae22c3aaafc58000079

def permute_a_palindrome (input):
    if input=="":
        return True
    max=len(input)%2 #0, 1
    s=''.join(sorted(input))
    count=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
            if count==len(input):
                return True
        else:
            max-=count%2
            if max<0:
                return False
            count=1
    return True