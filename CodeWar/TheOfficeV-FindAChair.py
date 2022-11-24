#https://www.codewars.com/kata/57f6051c3ff02f3b7300008b

def meeting(rooms, need):
    if need==0:
        return "Game On"
    for i in range(len(rooms)):
        rooms[i]=rooms[i][1]-len(rooms[i][0])
    a=sum(x for x in rooms if x>0)
    if a<need:
        return "Not enough!"
    ans=[]
    for i in range(len(rooms)):
        if need==0 or rooms[i]<0:
            ans.append(0)
        elif need>rooms[i]:
            need-=rooms[i]
            ans.append(rooms[i])
        else:
            ans.append(need)
            break
    return ans