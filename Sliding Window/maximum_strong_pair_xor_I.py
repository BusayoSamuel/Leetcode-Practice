"""
https://leetcode.com/problems/maximum-strong-pair-xor-i/description/
"""

class Solution: #Time complexity O(n^2), Space complexity O(1)
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i]-nums[j]) <= min(nums[i], nums[j]):
                    res = max(res, nums[i] ^ nums[j])

        return res