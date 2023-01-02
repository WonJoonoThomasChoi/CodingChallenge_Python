#https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numset = sorted(nums)
        print(numset)
        ans = []
        for i in range(len(numset)-2):
            lp = i+1
            rp = len(numset)-1
            target = 0 - numset[i]
            temp = []
            while lp<rp:
                if numset[lp]+numset[rp] == target:
                    if [numset[i],numset[lp],numset[rp]] not in ans:
                        ans.append([numset[i],numset[lp],numset[rp]])
                    lp+=1
                    rp-=1
                elif numset[lp]+numset[rp] > target:
                    rp-=1
                elif numset[lp]+numset[rp] < target:
                    lp+=1
        return ans

