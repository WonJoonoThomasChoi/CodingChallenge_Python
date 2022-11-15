#https://www.codewars.com/kata/52a112d9488f506ae7000b95

def is_int_array(arr):
    print(arr)
    if arr=="":
        return False
    if arr==None:
        return False
    if len(arr)==0:
        return True
    if None in arr:
        return False
    for i in arr:
        try:
            if int(i)!=i:
                return False
        except:
            return False
    return True