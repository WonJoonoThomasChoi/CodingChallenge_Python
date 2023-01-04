# https://www.acmicpc.net/problem/2456

import sys
candid1 = ""
candid2 = ""
candid3 = ""
n = int(sys.stdin.readline())
for _ in range(n):
    c1,c2,c3 = map(int,sys.stdin.readline().split())
    candid1 += str(c1)
    candid2 += str(c2)
    candid3 += str(c3)

candid1 = sorted(candid1, reverse=True)
candid2 = sorted(candid2, reverse=True)
candid3 = sorted(candid3, reverse=True)


candid1val=(sum(map(int,candid1)))
candid2val=(sum(map(int,candid2)))
candid3val=(sum(map(int,candid3)))

candid1 = int(str(candid1.count("3")*3 + candid1.count("2")*2 + candid1.count("1")) + ("".join(candid1)))
candid2 = int(str(candid2.count("3")*3 + candid2.count("2")*2 + candid2.count("1")) + ("".join(candid2)))
candid3 = int(str(candid3.count("3")*3 + candid3.count("2")*2 + candid3.count("1")) + ("".join(candid3)))

if candid1 == candid2 == candid3:
    print(0, candid1val)
elif candid1 > candid2 and candid1 > candid3:
    print(1, candid1val)
elif candid2 > candid1 and candid2 > candid3:
    print(2, candid2val)
elif candid3 > candid1 and candid3 > candid2:
    print(3, candid3val)
elif candid1 == candid2 and candid1 > candid3:
    print(0, candid1val)
elif candid1 == candid3 and candid1 > candid2:
    print(0, candid1val)
elif candid2 == candid3 and candid2 > candid1:
    print(0, candid2val)


