#https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def solution(args):
    ans=[]
    start=args[0]
    for i in range(1,len(args)):
        if args[i]-args[i-1]!=1:
            if start==args[i-1]:
                ans.append(str(start))
            else:
                if args[i-1]-start==1:
                    ans.append(str(start))
                    ans.append(str(args[i-1]))
                else:
                    ans.append(str(start) + "-" + str(args[i-1]))
            start=args[i]
    if args[i]-start==1:
        ans.append(str(start))
        ans.append(str(args[i]))
    elif args[i]==start:
        ans.append(str(start))
    else:
        ans.append(str(start)+"-"+str(args[i]))
    return ",".join(ans)