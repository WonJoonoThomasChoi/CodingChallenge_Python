#https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution:
    def minTimeToType(self, word: str) -> int:
        place=1
        ans=0
        fst = "a"
        for i in range(len(word)):
            snd = word[i]
            a=( abs(idx(fst)-idx(snd)) )
            b=(26 - ( max(idx(fst),idx(snd)) - min(idx(fst),idx(snd))))
            ans+=min(a,b)+1
            fst=word[i]
        return ans
def idx(char):
    return ord(char)-96