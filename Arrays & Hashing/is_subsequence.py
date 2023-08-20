"""
https://leetcode.com/problems/is-subsequence/description/
"""

class Solution1: #O(n) time complexity, #O(1) space complexity
    def isSubsequence(self, s: str, t: str) -> bool:
        s = s[::-1]

        if not s: #If s is already an empty string then it is a subsequence, regardless of if t is an empty string or not
            return True

        for i in range(len(t)):
            if s[-1] == t[i]:
                s = s[:-1]

            if not s:
                return True

        return False
    

class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0

        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1

        return p1 >= len(s)