"""
https://leetcode.com/problems/valid-parentheses/description/
"""
class Solution: #0(n) time complexity #O(n) space complexity
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
                "{": "}", 
                "(":")",
                "[":"]"
                }

        for i in range(len(s)):
            if s[i] in pairs:
                stack.append(pairs[s[i]])
            else:
                if not stack or s[i] != stack.pop(): # "if stack and s[i] != stack.pop()" wouldn't work for the edge case of a single bracket (e.g "]")
                    return False

        return len(stack) == 0