"""
https://leetcode.com/problems/two-sum/description/
"""

class Solution: #O(n) time complexity, #O(n) space complexity
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #value:index

        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target-nums[i]], i]
            
            hashmap[nums[i]] = i

class Solution: #O(n^2) time complexity, #O(1) space complexity
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
