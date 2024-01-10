"""
https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/description/
"""

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 0

        res = 1
        l = 0
        r = len(nums) - 1

        while l < len(nums) and nums[l] == 0:
            l += 1

        while r > -1 and nums[r] == 0:
            r -= 1

        while l <= r:
            if nums[l] == 1:
                l += 1
                count = 1
                while l <= r and nums[l] != 1:
                    count += 1
                    l += 1
                res *= count

        return res % (10 ** 9 + 7)
            
            
        