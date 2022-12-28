#https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        inc=sum=0
        while sum<n:
            inc+=1
            sum+=inc
        return inc-1 if sum!=n else inc
        