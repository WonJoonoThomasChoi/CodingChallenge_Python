# https://www.acmicpc.net/problem/1181

import sys

word_list = []

for _ in range (int(sys.stdin.readline())):
    temp_word = sys.stdin.readline().rstrip()
    if temp_word not in word_list:
        word_list.append(temp_word)
word_list.sort()
word_list.sort(key=len)
for i in word_list:
    print(i)