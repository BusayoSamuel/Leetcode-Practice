"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""
class Solution: #0(n) time complexity, #0(n) space complexity
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            
            hashset.add(s[r])
            res = max(res, r - l + 1)

        return res
