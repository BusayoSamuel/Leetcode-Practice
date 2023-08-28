"""
https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/
"""

class Solution: #O(nlogn) time complexity, #O(1) space complexity
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        l = 0
        res = float("Inf")

        for r in range(k-1, len(nums)):
            diff = nums[l] - nums[r]
            res = min(res, diff)

            l += 1

        return res