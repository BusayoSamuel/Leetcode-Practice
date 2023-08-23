"""
https://leetcode.com/problems/removing-stars-from-a-string/description/
"""

class Solution: #O(n) time complexity, #O(n) space complexity
    def removeStars(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] == "*":
                stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)