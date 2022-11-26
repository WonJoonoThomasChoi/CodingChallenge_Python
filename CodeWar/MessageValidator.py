#https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc

def is_a_valid_message(message):
    nums="1234567890"
    if message=="" :
        return True
    if message[0] not in nums:
        return False
    tleng="0"
    chars=""
    for i in range(len(message)):
        if message[i] in nums:
            if chars=="":
                tleng+=message[i]
            else:
                if int(tleng)!=len(chars):
                    return False
                else:
                    tleng=message[i]
                    chars=""
        else:
            chars+=message[i]
    return int(tleng)==len(chars)