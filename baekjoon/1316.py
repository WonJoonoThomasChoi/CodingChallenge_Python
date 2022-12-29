# https://www.acmicpc.net/problem/1316

def check(word):
    alist = []
    cur = word[0]
    for i in range(1, len(word)):
        if word[i] in alist:
            return 0
        if cur != word[i]:
            alist.append(cur)
            cur = word[i]
    return 1


count = 0
for i in range(int(input())):
    word = input()
    count += check(word)
print(count)
