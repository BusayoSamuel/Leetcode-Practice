"""
https://leetcode.com/problems/remove-element/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

        return l
    