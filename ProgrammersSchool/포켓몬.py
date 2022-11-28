#https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    alist=[]
    for num in nums:
        if num not in alist:
            alist.append(num)

    return min(len(alist),int(len(nums)/2))
