"""
https://leetcode.com/problems/house-robber-ii/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2
        
