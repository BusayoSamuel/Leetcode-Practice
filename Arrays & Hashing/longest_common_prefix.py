"""
https://leetcode.com/problems/longest-common-prefix/description/
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix