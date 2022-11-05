# https://www.codewars.com/kata/5966847f4025872c7d00015b

def average_string(s):
    s=s.split(" ")
    adict={}
    adict["zero"]="0"
    adict["one"]="1"
    adict["two"]="2"
    adict["three"]="3"
    adict["four"]="4"
    adict["five"]="5"
    adict["six"]="6"
    adict["seven"]="7"
    adict["eight"]="8"
    adict["nine"]="9"
    ans=0
    for i in range(len(s)):
        try:
            s[i]=s[i].replace(s[i],adict[s[i]])
        except:
            return "n/a"
        ans+=int(s[i])
    return ([k for k,v in adict.items() if v == str(ans/len(s))[0]])[0]