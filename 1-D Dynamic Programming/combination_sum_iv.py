"""
https://leetcode.com/problems/combination-sum-iv/description/
"""

class MySolution: #Time complexity O(nums * target), Space complexity O(target)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0
        dp = {}

        def dfs(target):
            nonlocal res

            if target in dp:
                return dp[target]

            if target < 0:
                return 0

            if target == 0:
                return 1

            total = 0

            for num in nums:
                total += dfs(target - num)

            dp[target] = total
            return dp[target]

            
        dfs(target)
        return dp[target]


class CleanerSolution: #Bottom-up approach, same complexity as above
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = { 0 : 1 }

        for total in range(1, target + 1):
            dp[total] = 0
            for num in nums:
                dp[total] += dp.get(total - num, 0)
        
        return dp[target]



            

        
