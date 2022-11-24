# https://www.codewars.com/kata/59752e1f064d1261cb0000ec

def what_time_is_it(angle):
    if angle//30 ==0:
        hour="12"
    elif angle//30<10:
        hour="0"+str(round(angle//30))
    else:
        hour=str(round(angle//30))
    if angle%30*2<10:
        minite="0"+str(int(angle%30*2))
    else:
        minite=str(int(angle%30*2))
    return hour+":"+minite