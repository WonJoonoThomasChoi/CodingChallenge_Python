# https://school.programmers.co.kr/learn/courses/30/lessons/42586

import math
def solution(progresses, speeds):
    answer, cmax, count = [], math.ceil((100 - progresses[0])/speeds[0]), 1
    for i in range(1,len(progresses)):
        if math.ceil((100 - progresses[i])/speeds[i])<=cmax:
            count+=1
        else:
            answer.append(count)
            cmax,count = math.ceil((100 - progresses[i])/speeds[i]),1
    answer.append(count)
    return answer