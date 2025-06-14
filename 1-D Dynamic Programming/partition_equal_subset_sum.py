"""
https://leetcode.com/problems/partition-equal-subset-sum/submissions/1663932862/
"""

class MyIneffecientSolution: #Timec complexity O(2^n), Space complexity O(n)
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums)//2
        curSum = 0

        def dfs(i):
            nonlocal curSum
            
            if curSum == target:
                return True

            if i >= len(nums):
                return False

            curSum += nums[i]
            if dfs(i+1):
                return True
            curSum -= nums[i]
            if dfs(i+1):
                return True

            return False

        return dfs(0)

class Solution: #Time complexity 0(n*sum(n), Space complexity O(sum(n))
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False
        
