# https://www.codewars.com/kata/5389864ec72ce03383000484

def autocomplete(inp, d):
    temp=""
    for i in inp.lower():
        if i in 'abcdefghijklmnopqrstuvwxyz':
            temp+=i
    inp=temp
    print(inp)
    alist=[]
    count=0
    print(inp[0:len(inp)])
    for i in d:
        if inp == i[0:len(inp)].lower() and count!=5:
            alist.append(i)
            count+=1
    print(alist)
    return alist