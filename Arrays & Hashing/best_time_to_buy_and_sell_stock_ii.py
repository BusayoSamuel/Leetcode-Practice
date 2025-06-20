"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
"""

class MySolution: #Time complexity O(n^2), Space complexity O(1)
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        res = 0

        while l < len(prices):
            diff = 0
            while r < len(prices) and prices[r] - prices[l] >= diff:
                diff = prices[r] - prices[l]
                r += 1 
            res += diff
            l = r

        return res

class CleanerSolution: #Time complexity O(n), Space complexity O(1)
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
            
        return profit
