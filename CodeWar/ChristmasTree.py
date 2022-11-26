#https://www.codewars.com/kata/52755006cc238fcae70000ed

def christmas_tree(height):
    if height==0:
        return ""
    alist=[]
    lmax=height-1
    for i in range(height):
        temp=""
        for j in range(height-1-i):
            temp+=" "
        while len(temp)!=lmax:
            temp+="*"
        alist.append(temp + "*" + temp[::-1])
    return ("\n".join(alist))