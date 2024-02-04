"""
https://leetcode.com/problems/maximum-number-of-balloons/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        balloon = Counter("balloon")

        res = float("Inf")

        for c in balloon:
            res = min(res, countText[c] // balloon[c])

        return res