"""
https://leetcode.com/problems/make-the-string-great/description/
"""


class Solution: #Time complexity O(n), Space complexity O(n)
    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:

            if (stack and 
                ((stack[-1] == c.lower() and c == c.upper()) or 
                (stack[-1] == c.upper() and c == c.lower()))):

                stack.pop()
                continue

            stack.append(c)

        return "".join(stack)

class OtherSolution: #Same complexity
    def makeGood(self, s: str) -> str:
        def lower(c):
            if ord(c) < ord('a'): #Therefore this is an uppercase letter
                return chr(ord('a') + ord(c) - ord('A')) 
            return c

        stack = []

        for c in s:
            if (stack
                and stack[-1] != c
                and lower(stack[-1]) == lower(c)
                ):
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

        
