"""
https://leetcode.com/problems/integer-break/description/
"""

class MySolution: #Time complexity O(n^n), Space complexity O(n)
    def integerBreak(self, n: int) -> int:
        dp = {0:1}

        def dfs(target):
            if target in dp:
                return dp[target]

            prod = 1
            for i in range(2, n):
                if i > target:
                    break
                
                prod = max(prod, i * dfs(target - i))

            dp[target] = prod

            return dp[target]

        return dfs(n)
