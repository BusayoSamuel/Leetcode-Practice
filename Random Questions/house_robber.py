"""
https://leetcode.com/problems/house-robber/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2]) #key line, maintains the best option between adding the money two indexes ahead or skipping to the next index

        return dp[-1]
