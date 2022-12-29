# https://www.acmicpc.net/problem/10250

#cases = int(input())

'''
10 10 100
10 10 99

1010
910
'''

for i in range(int(input())):
    h, w, n = map(int, input().split())
    room = n//h + 1
    floor = n % h
    if n % h == 0:  # h의 배수이면,
        room = n//h
        floor = h
    print(str(floor)+(str(room) if len(str(room))==2 else "0"+str(room)))