#https://www.codewars.com/kata/58068479c27998b11900056e

def sort_twisted37(arr):
    for i in range(2):
        arr=sorted(arr)
        for i in range(len(arr)):
            arr[i]=str(arr[i])
        arr="   ".join(arr)
        arr=change(arr,"7","3")
        arr=arr.split("   ")
        for i in range(len(arr)):
            arr[i]=int(arr[i])
    return arr

def change(total, string1, string2):
    return total.replace(string1,"asdf").replace(string2,string1).replace("asdf",string2)
