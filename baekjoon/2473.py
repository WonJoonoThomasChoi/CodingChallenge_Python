# https://www.acmicpc.net/problem/2473

import sys
n = int(sys.stdin.readline())
diff = 3000000000
nums = sorted(list(map(int, sys.stdin.readline().split())))

def solution(arr, num3):
    lp = 0
    rp = len(arr) - 1
    global result
    global diff
    while lp<rp:
        temp = arr[lp] + arr[rp] + num3
        if abs(temp) < diff:
            diff = abs(temp)
            result = [arr[lp], arr[rp], num3]
        elif temp > 0:
            rp-=1
        elif temp < 0:
            lp+=1
        else:
            break


for i in range(len(nums)):
    solution(nums[i+1:], nums[i])
print(*sorted(result))