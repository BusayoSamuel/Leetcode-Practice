"""
https://leetcode.com/problems/maximum-subarray-min-product/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        res = 0
        stack = []

        for i, num in enumerate(nums):
            new_start = i
            while stack and stack[-1][1] > num:
                start, val = stack.pop()
                total = prefix[i] - prefix[start]
                res = max(res, val * total)
                new_start = start
            stack.append((new_start, num))

        while stack:
            start, val = stack.pop()
            total = prefix[n] - prefix[start]
            res = max(res, val * total)

        return res % (10**9 + 7)
