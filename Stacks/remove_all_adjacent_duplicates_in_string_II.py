"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for i in range(len(s)):
            if stack and stack[-1][0] == s[i]:
                stack[-1] += s[i]
                if len(stack[-1]) == k:
                    stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)