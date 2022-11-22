#https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    return sorted([x for x in arr if x%divisor==0]) if len(sorted([x for x in arr if x%divisor==0]))!=0 else [-1]