# https://www.acmicpc.net/problem/17609

import sys


def s_palindrome(str):
    lp, rp = 0, len(str) - 1
    while lp < rp:
        if str[lp] == str[rp]:
            lp += 1
            rp -= 1
        elif str[lp] != str[rp]:
            return 1 if (True if str[lp + 1:rp + 1] == str[lp + 1:rp + 1][::-1] else False) or (
                True if str[lp:rp] == str[lp:rp][::-1] else False) else 2


for _ in range(int(sys.stdin.readline())):
    String = sys.stdin.readline().rstrip()
    if String == String[::-1]:
        print(0)
    else:
        print(s_palindrome(String))

    '''
21
abbab
aab
aaab
aaaab
aaaaab
aaaaaab
axaaxaa
abcddadca
aabcbcaa
ababbabaa
abca
babba
sumumuus
XYXYAAYXY
abc
cccfccfcc
abcddcdba
ppbpppb
aabcdeddcba
aabab
aapqbcbqpqaa

1
1
1
1
1
1
1
2
1
1
1
1
1
1
2
1
1
2
2
2
1
    '''
