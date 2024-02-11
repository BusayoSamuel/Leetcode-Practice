"""
https://leetcode.com/problems/word-pattern/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        cToW = {}
        wToC = {}

        for c, w in zip(pattern, words):
            if c in cToW and cToW[c] != w:
                return False

            if w in wToC and wToC[w] != c:
                return False

            cToW[c] = w
            wToC[w] = c

        return True