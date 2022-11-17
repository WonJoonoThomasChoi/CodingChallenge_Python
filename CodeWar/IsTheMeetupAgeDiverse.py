#https://www.codewars.com/kata/5829ca646d02cd1a65000284

def is_age_diverse(lst):
    if len(lst)<10:
        return False
    alist=[]
    for a in lst:
        alist.append(int(a['age']/10))
    if max(alist) not in range(10,19):
        return False
    for i in range(1,10):
        if i not in alist:
            return False
    return True