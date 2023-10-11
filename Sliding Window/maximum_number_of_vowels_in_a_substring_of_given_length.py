"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
"""
class Solution: #Time complexity O(n), Space Complexity O(1)
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        l = 0
        res = 0
        count = 0
        for r in range(len(s)):
            if s[r] in vowels:
                count += 1          

            if r - l == k:
                if s[l] in vowels:
                    count -= 1
                l += 1

            res = max(res, count)

        return res


        