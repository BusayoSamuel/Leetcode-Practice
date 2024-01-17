"""
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/
"""

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        unique = set()

        for i in range(len(nums)):
            if nums[i] in unique:
                return nums[i]

            unique.add(nums[i])