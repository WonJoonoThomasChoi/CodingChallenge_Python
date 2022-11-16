#https://www.codewars.com/kata/51f1342c76b586046800002a

ef solution(n):
rem=0
num=int(str(n).split(".")[0])
dec=n-num
if dec<0.25:
    dec=0
elif dec>=0.25 and dec<0.75:
    dec=0.5
else:
    dec=0
    rem+=1
return num+dec+rem