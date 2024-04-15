"""
https://leetcode.com/problems/removing-stars-from-a-string/description/
"""

class Solution: #O(n) time complexity, #O(n) space complexity
    def removeStars(self, s: str) -> str:
        stack = []

        for c in s: #better to reference the characters directly instead of using index i.e for i in range(len(s))....
            if c == "*":
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


class OtherSolution: #Same complexity but strings were mutable you could get by with O(1) space
    def removeStars(self, s: str) -> str:
        s = [*s]
        l = 0 #use l to keep track of where the next character to be replaced is

        for r in range(len(s)):
            if s[r] == "*":
                l -= 1     
            else:
                s[l] = s[r]
                l += 1
            

        return "".join(s[:l])
