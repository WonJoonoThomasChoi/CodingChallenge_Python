#https://www.codewars.com/kata/5839c48f0cf94640a20001d3

def land_perimeter(arr):
    ans=0
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x]=="X":
                ans+= check(y,x,arr)
    return "Total land perimeter: " + str(ans)

def check(y,x,arr):
    count=4
    if y-1>=0:
        if arr[y-1][x]=="X":
            count-=1
    if y+1<len(arr):
        if arr[y+1][x]=="X":
            count-=1
    if x-1>=0:
        if arr[y][x-1]=="X":
            count-=1
    if x+1<len(arr[0]):
        if arr[y][x+1]=="X":
            count-=1
    return count