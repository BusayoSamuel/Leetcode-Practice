"""
https://leetcode.com/problems/sort-colors/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                #we don't increment the i pointer here to ensure that we don't skip a potential zero, i is always ahead of l so we can be sure that l will always be resting on a 1 or 0
            else:
                i += 1

        return nums
        