"""
https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def minSwaps(self, s: str) -> int:
        close = maxClose = 0

        for c in s:
            if c == '[':
                close -= 1
            else:
                close += 1
            maxClose = max(maxClose, close)

        return (maxClose + 1) // 2
