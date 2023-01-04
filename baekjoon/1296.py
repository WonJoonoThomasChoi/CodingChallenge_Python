# https://www.acmicpc.net/problem/1296
import sys


cmax = -1
maxName=""
myName = sys.stdin.readline().rstrip()

n = int(sys.stdin.readline())

for i in range(n):
    name = sys.stdin.readline().rstrip()
    L=myName.count("L")+name.count("L")
    O=myName.count("O")+name.count("O")
    V=myName.count("V")+name.count("V")
    E=myName.count("E")+name.count("E")
    P = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
    if P > cmax:
        maxName = name
        cmax = P
    elif P==cmax:
        if name < maxName:
            maxName = name
            cmax = P
print(maxName)
