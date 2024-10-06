"""
https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/
"""

class MySolution: #Time complexity O(nm), Space complexity O(1) where n is the number of words and m is the average length of words
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(s):
            l = 0
            r = len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        for word in words:
            if isPalindrome(word):
                return word

        return ""


class AlternativeSolution: #Same complexity
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            l, r = 0, len(word) - 1
            while word[l] == word[r]:
                if l >= r:
                    return word
                l, r = l + 1, r - 1
        return ""



        
