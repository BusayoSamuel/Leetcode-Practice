"""
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
"""

class Solution: #Time complexity O(k*2^n), Space complexity O(n)
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)

        def backtrack(i, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return backtrack(0, k - 1, 0)
            for j in range(i, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                used[j] = True
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                used[j] = False
            return False

        return backtrack(0, k, 0)


class MySolution: #Time complexity O(k^n), Space complexity O(n), Not as efficient as above
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        target = sum(nums) // k
        res = [0 for i in range(k)]

        def dfs(i):
            if i >= len(nums):
                return True

            if nums[i] > target:
                return False

            for j in range(len(res)):
                if res[j] + nums[i] > target:
                    continue
                
                res[j] += nums[i]
                if dfs(i + 1):
                    return True
                res[j] -= nums[i]

            return False

        return dfs(0)


