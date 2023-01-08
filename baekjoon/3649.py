# https://www.acmicpc.net/problem/3649

import sys

while True:
    try:
        target = int(sys.stdin.readline()) * 10000000
        n = int(sys.stdin.readline())
        nums = sorted([int(sys.stdin.readline()) for _ in range(n)])
        lp, rp = 0, n - 1
        while lp < rp:
            if nums[lp] + nums[rp] == target:
                print("yes", nums[lp], nums[rp])
                break
            elif nums[lp] + nums[rp] < target:
                lp += 1
            else:
                rp -= 1
        else:
            print("danger")
    except:
        break
