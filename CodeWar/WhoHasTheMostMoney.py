# https://www.codewars.com/kata/528d36d7cc451cd7e4000339
def most_money(students):
    if len(students)==1:
        return students[0].name
    max=0
    candid=""
    alist=[]
    for student in students:
        temp=0
        temp+=student.twenties*20
        temp+=student.tens*10
        temp+=student.fives*5
        alist.append(temp)
        if temp>max:
            max=temp
            candid=student.name
    for i in range(len(alist)):
        for j in range(i+1,len(alist)):
            if alist[i]!=alist[j]:
                return candid
    return "all"