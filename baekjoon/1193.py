# https://www.acmicpc.net/problem/1193
n = int(input())

count = 1
line = 1
while n > count:
    line += 1
    count += line
left = n - count + line
right = line - left + 1
if line % 2 == 0:
    print(str(left) + "/" + str(right))
else:
    print(str(right) + "/" + str(left))
