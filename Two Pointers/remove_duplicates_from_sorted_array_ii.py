"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
"""

class Solution1: #Time complexity O(n), Space complexity O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1

        if len(nums) == 1:
            return l
 
        count = 1

        for r in range(1, len(nums)):
            if nums[r] == nums[l-1]:
                if count != 2:
                    nums[r], nums[l] = nums[l], nums[r]
                    count += 1
                    l += 1
            else:
                count = 1
                nums[r], nums[l] = nums[l], nums[r]
                l += 1

        return l
    
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r + 1]: #count the number of duplicates
                r += 1
                count += 1
            
            for i in range(min(2, count)): #move a maximum of 2 to the left
                nums[l] = nums[r]
                l += 1
            r += 1 #move on to the next set of possible duplicates
        return l
