# https://www.acmicpc.net/problem/10769

import sys
txt = sys.stdin.readline().rstrip()
happy = txt.count(":-)")
sad = txt.count(":-(")
if happy==0 and sad==0:
    print("none")
elif happy>sad:
    print("happy")
elif happy<sad:
    print("sad")
else:
    print("unsure")