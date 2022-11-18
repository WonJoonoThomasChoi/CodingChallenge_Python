#https://www.codewars.com/kata/51f41fe7e8f176e70d0002b9

def sortme(words):
    print(words)
    temp=[]
    for i in range(len(words)):
        temp.append(words[i].lower())
    temp=sorted(temp)
    temp2=temp.copy()

    for i in range(len(words)):
        ind=temp.index(words[i].lower())
        temp2[ind]=words[i]
    return (temp2)