"""
https://leetcode.com/problems/longest-repeating-character-replacement/description/
"""

class Solution: #O(n) time complexity, #O(n) space complexity
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #letters : count
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1


            while ((r - l  + 1) - max(count.values())) > k: #within a window, you'd ideally replace the least common letters, so k is compared to the number of least common letters
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res