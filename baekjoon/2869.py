# https://www.acmicpc.net/problem/2869


import math
nums = list(map(int, input().split()))
reach = nums[2] - nums[0]
diff = nums[0] - nums[1]
print(math.ceil(reach / diff)+1)

