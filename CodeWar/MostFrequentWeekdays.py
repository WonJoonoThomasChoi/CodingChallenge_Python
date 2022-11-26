#https://www.codewars.com/kata/56eb16655250549e4b0013f4

import datetime
def most_frequent_days(year):
    mon,tue,wed,thu,fri,sat,sun=0,0,0,0,0,0,0
    ans=[0,0,0,0,0,0,0]
    for i in range(1,13):
        for j in range(1,32):
            try:
                ans[datetime.datetime(year,i,j).weekday()]+=1
            except:
                pass
    ans2=[]
    for i in range(len(ans)):
        if ans[i]==max(ans):
            if i==0:
                ans2.append('Monday')
            elif i==1:
                ans2.append('Tuesday')
            elif i==2:
                ans2.append('Wednesday')
            elif i==3:
                ans2.append('Thursday')
            elif i==4:
                ans2.append('Friday')
            elif i==5:
                ans2.append('Saturday')
            elif i==6:
                ans2.append('Sunday')
    return ans2