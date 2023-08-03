"""
https://leetcode.com/problems/search-insert-position/description/
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r)//2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        
        return m + 1 if nums[m] < target else  m  #not "return m + 1 if nums[m] < target else return m". 
    #Just returning m wouldn't work because if nums[m] is less than target, the target has to be placed ahead of it 