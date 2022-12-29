# https://www.acmicpc.net/problem/1712

nums = list(map(int, input().split()))
diff=nums[2]-nums[1]
if diff<=0:
    print(-1)
elif nums[0]<=0:
    print (0)
else:
    print (int(nums[0] / diff)+1)
