"""
https://leetcode.com/problems/subarray-sum-equals-k/description/
"""

class MySolution: #Time complexity O(n^2), Space complexity O(1)
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        l = 0
        res = 0

        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total == k:
                    res += 1

        return res

class EfficientSolution: # Time complexity O(n), Space complexity O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = curSum = 0
        prefixSums = { 0 : 1 }

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        
        return res
        
