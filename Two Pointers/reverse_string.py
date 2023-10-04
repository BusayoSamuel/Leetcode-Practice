"""
https://leetcode.com/problems/reverse-string/description/
"""

class Solution: #Time complexity O(n), #Space complexity O(1)
    def reverseString(self, s: List[str]) -> None:
         l = 0
         r = len(s) - 1

         while l <= r:
             temp = s[l]
             s[l] = s[r]
             s[r] = temp
             l += 1
             r -= 1

        