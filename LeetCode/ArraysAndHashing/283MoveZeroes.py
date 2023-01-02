# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lp = 0
        alist=[0] * len(nums)
        print(alist)
        for i in nums:
            if i!=0:
                alist[lp]=i
                lp+=1
        for i in range(len(alist)):
            nums[i] = alist[i]
        





