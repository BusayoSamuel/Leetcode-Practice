"""
https://leetcode.com/problems/uncrossed-lines/description/
"""

class Solution:#Time complexity O(n*m), Space complexity O(n*m)
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = {}

        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            if nums1[i] == nums2[j]:
                dp[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = max(dfs(i, j + 1), dfs(i + 1, j))

            return dp[(i, j)]

        return dfs(0, 0)
