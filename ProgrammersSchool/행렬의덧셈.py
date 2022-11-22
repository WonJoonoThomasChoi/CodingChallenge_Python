#https://school.programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    ans=[]
    for j in range(len(arr1)):
        temp=[]
        for i in range(len(arr1[j])):
            temp.append(arr1[j][i]+arr2[j][i])
        ans.append(temp)
    return ans

