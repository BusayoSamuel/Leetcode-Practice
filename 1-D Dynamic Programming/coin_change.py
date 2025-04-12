"""
https://leetcode.com/problems/coin-change/description/
"""

class MyInefficientSolution: #Time complexity O(coins^amount), Space complexity O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = math.inf

        def dfs(total, i):
            nonlocal res
            
            if total > amount:
                return 

            if total == amount:
                res = min(res, i)

            for coin in coins:
                dfs(total + coin, i + 1)

        dfs(0, 0)
        return res if res != math.inf else -1

            
        

class MySolution: #Top-Down approach, Time complexity O(coins * amount), Space complexity(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(curAmount):
            if curAmount < 0:
                return math.inf

            if curAmount in dp:
                return dp[curAmount]
            
            if curAmount == 0:
                return 0

            res = math.inf

            for coin in coins:
                res = min(res, 1 + dfs(curAmount - coin))

            dp[curAmount] = res

            return res

        dfs(amount)
        if amount not in dp:
            return 0
            
        return dp[amount] if dp[amount] != math.inf else -1


class CleanerSolution: #Bottom-up approach, Same complexity as above
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

            
        
