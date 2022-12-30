# https://www.acmicpc.net/problem/1427

import sys
print( "".join(sorted([x for x in str(int(sys.stdin.readline()))], reverse=True)))