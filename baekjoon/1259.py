#https://www.acmicpc.net/problem/1259

import sys

def isPalindrome(str):
    lp, rp = 0, len(str)-1
    while lp<rp:
        if str[lp] != str[rp]:
            return "no"
        else:
            lp+=1
            rp-=1
    return "yes"


while True:
    temp = int(sys.stdin.readline())
    if temp == 0:
        break
    else:
        print(isPalindrome(str(temp)))

