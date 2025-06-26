"""
https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1

        while l < r and s[l] == s[r]:
            tmp = s[l]

            while l <= r and s[l] == tmp:
                l += 1
            while l <= r and s[r] == tmp:
                r -= 1

        return r - l + 1

class MySolution: #Same complexity as above
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1


        while l < r and s[l] == s[r]:
            while l < r and s[l+1] == s[l]:
                l += 1
            while r > l and s[r-1] == s[r]:
                r -= 1
            l += 1
            r -= 1

        return 0 if l > r else r - l + 1
        
        
