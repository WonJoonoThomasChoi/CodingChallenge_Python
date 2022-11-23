#https://school.programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    ans=[]
    for i in range(len(commands)):
        ans.append(sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1])
    return ans