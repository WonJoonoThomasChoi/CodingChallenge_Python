#https://school.programmers.co.kr/learn/courses/30/lessons/12901

import datetime
def solution(a, b):
    adict={0:"MON",1:"TUE",2:"WED",3:"THU",4:"FRI",5:"SAT",6:"SUN"}
    x=datetime.datetime(2016,a,b)
    return adict[x.weekday()]