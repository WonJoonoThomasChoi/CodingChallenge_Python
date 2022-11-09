# https://www.codewars.com/kata/5583d268479559400d000064

def binary_to_string(binary):
    alist=[]
    ans=""
    for i in range(int(len(binary)/8)):
        ans+=chr(int(binary[8*i:8*(i+1)],2))
    return ans