# https://www.codewars.com/kata/5a946d9fba1bb5135100007c

def minimum_number(numbers):
    count=0
    a=(sum(numbers))
    while (fprime(a+count)==False):
        count+=1
    return count



def fprime(n):
    if n<=1:
        return False
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True