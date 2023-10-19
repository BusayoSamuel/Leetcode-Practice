"""
https://leetcode.com/problems/find-peak-element/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l<=r:
            m = (r+l)//2

            if m - 1 >= 0 and nums[m-1] > nums[m]:
                r = m - 1
            elif m + 1 < len(nums) and nums[m+1] > nums[m]:
                l = m + 1
            else:
                return m 
        