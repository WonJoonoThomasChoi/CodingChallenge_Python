# https://www.acmicpc.net/problem/5622

alst = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
letters = input()
for i in range(len(alst)):
    letters = letters.replace(alst[i], str(i))
print(len(letters))
