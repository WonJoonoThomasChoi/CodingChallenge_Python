#https://www.codewars.com/kata/557e8a141ca1f4caa70000a6

def is_triangle_number(number):
    print(number)
    if (isAbs(number)!=True):
        return False
    if number<=0:
        return True
    # 1,2,4,7,11,16
    start=1
    end=1
    i=1
    while start<number:
        i+=1
        start+=i
    print(number, start)
    return number==start
    # 1,3,6,10,15,21

def isAbs(n):
    try:
        if int(n)!=n:
            return False
    except:
        return False
    return True