"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (r + l)//2
            if nums[m] == target:
                return True

            if nums[m] < nums[l]: #you have to keep your reference to l constant
                if target > nums[m] and target <= nums[r]:
                    l = m + 1 
                else:
                    r = m - 1
            elif nums[m] > nums[l]: #you have to keep your reference to l constant
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                l += 1
        
        return False
        
        