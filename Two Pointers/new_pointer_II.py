"""
https://leetcode.com/problems/valid-palindrome-ii/description/
"""

class Solution1: #O(n) time complexity, #O(1) space complexity
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return self.isValid(s[l:r]) or self.isValid(s[l+1:r+1]) # "r+1" ensures that the character at s[r] is included

            l += 1
            r -= 1

        return True


    def isValid(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                print(s[l])
                print(s[r])
                return False

            l += 1
            r -= 1

        return True
    

class Solution2: #O(n) time complexity, #O(1) space complexity
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                skipR = s[l:r]
                skipL = s[l+1:r+1]
                return skipR == skipR[::-1] or skipL == skipL[::-1]

            l += 1
            r -= 1

        return True
