class MySolution: #Time complexity O(n) due to memoization, Space complexity O(n)
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i in dp:
                return dp[i]
                
            if i >= len(nums):
                return 0

            select = nums[i] + dfs(i+2)
            skip = dfs(i+1)

            dp[i] = max(select, skip)

            return dp[i]

        return dfs(0)
