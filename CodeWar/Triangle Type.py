# https://www.codewars.com/kata/53907ac3cd51b69f790006c5

# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    alist=[a,b,c]
    alist=sorted(alist)
    print(alist)
    if alist[0]+alist[1]<=alist[2]:
        return 0
    if (alist[0]**2)+(alist[1]**2)==alist[2]**2:
        return 2
    elif (alist[0]**2)+(alist[1]**2)>alist[2]**2:
        return 1
    elif (alist[0]**2)+(alist[1]**2)<alist[2]**2:
        return 3