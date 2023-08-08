"""
https://leetcode.com/problems/contains-duplicate-ii/description/
"""

class Solution: #O(n) time complexity, #O(1) space complexity
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {} #val : indices
        l = 0
        
        for r in range(len(nums)):
            if r - l > k:
                del hashmap[nums[l]]
                l += 1

            if nums[r] in hashmap:
                return True

            hashmap[nums[r]] = r

        return False