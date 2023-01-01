# https://www.acmicpc.net/problem/1924

import sys
import datetime

week_list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
m, d = list(map(int, sys.stdin.readline().split()))
print(week_list[datetime.date(2007, m, d).weekday()])
