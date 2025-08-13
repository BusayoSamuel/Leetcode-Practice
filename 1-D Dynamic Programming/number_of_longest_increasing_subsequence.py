"""
https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
"""


class Solution: #Time complexity O(n^2), Space complexity O(n)
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        lenLIS, res = 0, 0

        for i in range(n - 1, -1, -1):
            maxLen, maxCnt = 1, 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, count
                    elif length + 1 == maxLen:
                        maxCnt += count

            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt
            dp[i] = [maxLen, maxCnt]

        return res
