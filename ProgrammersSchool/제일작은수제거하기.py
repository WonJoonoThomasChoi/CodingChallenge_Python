#https://school.programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    if len(arr)==1:
        return [-1]
    del arr[arr.index(min(arr))]
    return arr
    #arr=arr.remove(min(arr))
