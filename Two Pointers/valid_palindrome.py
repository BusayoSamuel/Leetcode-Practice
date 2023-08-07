"""
https://leetcode.com/problems/valid-palindrome/description/
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() 
        l = 0
        r = len(s) - 1

        def isAlphaNum(c): #local functions have to be defined before they can be used, unless they are class methods
            if ((ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('0') and ord(c) <= ord('9'))):
                return True
            else:
                return False
            
        while l <= r:
            while l < r and not isAlphaNum(s[l]): #Need the added condition of while l < r to prevent the left and right pointers crossing each other
                l += 1

            while l < r and not isAlphaNum(s[r]):
                r -= 1

            if s[l] != s[r]: #Need to set s.lower() at the start, rather than inside the isAlphaNum function, to prevent this line from tripping
                return False 

            l += 1
            r -= 1

        return True