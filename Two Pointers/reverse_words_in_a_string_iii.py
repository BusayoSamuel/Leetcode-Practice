"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def reverseWords(self, s: str) -> str:
        l = 0
        s = [*s]

        for i in range(len(s) + 1):
            if i == len(s) or s[i] == " ":
                r = i - 1
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                l = i + 1

        return "".join(s)


class Solution: #Same complexity
    def reverseWords(self, s: str) -> str:
        l = 0
        s = [*s]

        for i in range(len(s)):
            if i == len(s) - 1 or s[i] == " ":
                r = i - 1
                if i == len(s) - 1:
                    r = i
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                l = i + 1

        return "".join(s)


        


        
