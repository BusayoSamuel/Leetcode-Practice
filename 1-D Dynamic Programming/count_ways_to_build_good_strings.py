"""
https://leetcode.com/problems/count-ways-to-build-good-strings/description/
"""

class MyInefficientSolution: #Time complexity O(2^n), Space complexity O(n)
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        cur = []
        res = 0

        def dfs():
            nonlocal res

            if len(cur) > high:
                return 

            if low <= len(cur) <= high:
                res += 1

            for _ in range(one):
                cur.append('1')
            dfs()

            for _ in range(one):
                cur.pop()

            for _ in range(zero):
                cur.append('0')
            dfs()

            for _ in range(zero):
                cur.pop()
            
        dfs()
        return res

class Solution: #Time complexity O(n), Space complexity O(n)
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = {}

        def dfs(length):
            if length > high:
                return 0
            if length in dp:
                return dp[length]

            dp[length] = 1 if length >= low else 0
            dp[length] += dfs(length + zero) + dfs(length + one)
            return dp[length] % mod

        return dfs(0)
        
