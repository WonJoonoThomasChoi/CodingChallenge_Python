#https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    sa = [1,2,3,4,5]
    aScore=0
    sb = [2,1,2,3,2,4,2,5]
    bScore=0
    sc = [3,3,1,1,2,2,4,4,5,5]
    cScore=0
    for i in range(len(answers)):
        if sa[i%len(sa)]==answers[i]:
            aScore+=1
        if sb[i%len(sb)]==answers[i]:
            bScore+=1
        if sc[i%len(sc)]==answers[i]:
            cScore+=1
    alist = {1:aScore, 2:bScore, 3:cScore}
    return [ k for k, v in alist.items() if v == max(alist.values())]