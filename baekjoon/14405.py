# https://www.acmicpc.net/problem/14405



import sys
print("YES" if len(sys.stdin.readline().rstrip().replace("pi","%").replace("ka","%").replace("chu","%").replace("%",""))==0 else "NO")