# https://www.acmicpc.net/problem/4949

import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s==".":
        break
    ns = ""
    for i in s:
        if i in "([)]":
            ns += i
    for i in range(100):
        ns=ns.replace("()", "")
        ns=ns.replace("[]", "")
        if ns=="":
            break
    if ns == "":
        print("yes")
    else:
        print("no")