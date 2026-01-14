"""
https://neetcode.io/solutions/knight-dialer
"""

class Solution: #Time complexity O(n), Space complexity O(10) -> O(1)
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10

        mod = 1000000007
        jumps = [
            [4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9],
            [], [0, 1, 7], [2, 6], [1, 3], [2, 4]
        ]

        dp = [1] * 10
        for step in range(n - 1):
            next_dp = [0] * 10
            for d in range(10):
                for j in jumps[d]:
                    next_dp[j] = (next_dp[j] + dp[d]) % mod
            dp = next_dp

        res = 0
        for d in dp:
            res = (res + d) % mod
        return res
