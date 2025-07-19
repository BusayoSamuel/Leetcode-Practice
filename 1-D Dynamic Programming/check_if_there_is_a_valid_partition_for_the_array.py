"""
https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def validPartition(self, nums: List[int]) -> bool:
        dp = { len(nums) : True }
        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = False
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                res = dfs(i + 2)
            if i < len(nums) - 2:
                if ((nums[i] == nums[i + 1] == nums[i + 2]) or 
                    (nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2])
                ):
                    res = res or dfs(i + 3)
            
            dp[i] = res
            return res
        
        return dfs(0)

class Solution: #Time complexity O(n), Space complexity O(1)
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False, True, True]

        for i in range(len(nums) - 2, -1, -1):
            dp1 = dp[0]
            if nums[i] == nums[i + 1] and dp[1]:
                dp[0] = True
            elif i < len(nums) - 2 and dp[2] and (
                (nums[i] == nums[i + 1] == nums[i + 2]) or 
                (nums[i] + 1 == nums[i + 1] and nums[i + 1] == nums[i + 2] - 1)
            ):
                dp[0] = True
            else:
                dp[0] = False
            dp[2] = dp[1]
            dp[1] = dp1

        return dp[0]


