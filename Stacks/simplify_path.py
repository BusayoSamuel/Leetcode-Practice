"""
https://leetcode.com/problems/simplify-path/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""

        for c in path:
            if c != "/":
                curr += c
            else:
                if curr == "..":
                    if stack: stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""

        return "/" + "/".join(stack)