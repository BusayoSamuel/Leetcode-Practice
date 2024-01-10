"""
https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        subtotal = 0
        nums.sort(reverse=True)
        res = []

        for i in range(len(nums)):
            res.append(nums[i])
            total -= nums[i]
            subtotal += nums[i]

            if subtotal > total:
                return res