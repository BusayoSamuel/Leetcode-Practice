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