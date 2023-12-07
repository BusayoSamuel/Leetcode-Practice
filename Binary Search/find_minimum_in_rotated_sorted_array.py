"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = 5000

        while l <= r:
            if nums[l] < nums[r]: #takes care of a scenario where the array is isn't rotated 
                res = min(res, nums[l])
                break

            m = (r + l)//2
            res = min(res, nums[m])
            if  nums[m] < nums[l]: #this means the lower sorted half is to the right
                r = m - 1
            else: 
                l = m + 1

        return res