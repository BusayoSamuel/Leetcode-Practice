"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""


class Solution: #Time complexity O(n), #Space complexity O(n)
    def removeDuplicates(self, nums: List[int]) -> int:
        hashset = set()
        l = 0
        
        for r in range(len(nums)):
            if nums[r] not in hashset:
                nums[l] = nums[r]
                l += 1
            hashset.add(nums[r])
            

        return len(hashset)
        


class BetterSolution: #Time complexity O(n), Space complexity O(1) 
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        for r in range(1, len(nums)):
            if nums[l-1] != nums[r]:
                nums[l] = nums[r]
                l += 1

        return l #nums always has a size of a least 1