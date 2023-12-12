"""
https://leetcode.com/problems/longest-nice-substring/description/
"""

class Solution: #Time complexity 0(n^2), Space complexity O(1)
    def longestNiceSubstring(self, s: str) -> str:
        res = []

        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(set(s[i:j+1])) % 2 == 0:
                    upcase = s[i:j+1].upper()
                    if len(set(s[i:j+1])) == len(set(upcase)) * 2:
                        if not res or max(res[1], j-i+1) != res[1]:
                            res = [s[i:j+1], j-i+1]


        return res[0] if res else ""