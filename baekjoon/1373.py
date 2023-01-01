# https://www.acmicpc.net/problem/1373

import sys

binary_num=str(sys.stdin.readline())
octal_num = int(binary_num, 2)
octal_str = oct(octal_num)
print(int(octal_str[2:]))