"""
https://leetcode.com/problems/climbing-stairs/description/
"""

class MySolution: #Time complexity O(2^n), Space complexity O(n)
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i > n:
                return 0

            if i == n:
                return 1

            return 0 + dfs(i+1) + dfs(i+2)

        return dfs(0)


class MySolution: #Time complexity O(n), Space complexity O(n)
    def climbStairs(self, n: int) -> int:
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
                
            if i > n:
                return 0

            if i == n:
                return 1

            dp[i] = (0 + dfs(i+1)) + (0 + dfs(i+2))

            return dp[i]

        return dfs(0)

class MostEffecientSolution: #Time complexity O(n), Space complexity O(1)
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]

        for i in range(n-1):
            temp = dp[0]
            dp[0] = dp[0] + dp[1]
            dp[1] = temp

        return dp[0]

