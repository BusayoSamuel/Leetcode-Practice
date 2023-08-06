"""
https://leetcode.com/problems/contains-duplicate/submissions/
"""

class Solution1: # O(1) time complexity, O(n) space complexity
    def containsDuplicate(self, nums: List[int]) -> bool:
        distincts = set(nums)
        return len(distincts) != len(nums)
    
class Solution2: # O(n) time complexity, O(n) space complexity
    def containsDuplicate(self, nums: List[int]) -> bool:
        distincts = set()
        for i in range(len(nums)):
            if nums[i] in distincts:
                return True
            distincts.add(nums[i])

        return False