"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""

class Solution: #O(n) time complexity, #O(1) space complexity
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0

        for r in range(len(prices)):
            res = max(res, prices[r] - prices[l])

            if prices[l] > prices[r]:
                l = r

        return res
    

