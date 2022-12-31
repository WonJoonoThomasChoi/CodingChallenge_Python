# https://www.acmicpc.net/problem/1476
import sys
print(6916/28)

tE, tS, tM = list(map(int,sys.stdin.readline().split()))
E = S = M = 0
count = 0
while True:
    E+=1
    S+=1
    M+=1
    if E>15:
        E=1
    if S>28:
        S=1
    if M>19:
        M=1
    count+=1
    if E==tE and S==tS and M==tM:
        print(count)
        break

