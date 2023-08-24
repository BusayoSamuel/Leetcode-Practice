"""
https://leetcode.com/problems/single-element-in-a-sorted-array/description/
"""

class Solution: #O(logn) time complexity, #O(1) space complexity 
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r:
            m = (l + r)//2

            if m + 1 < len(nums) and nums[m] == nums[m+1]:
                if (r - m) % 2 == 0:  #if the right side is an even size then there must be an element that only appears once there
                    l = m + 2
                else:
                    r = m - 1
            elif m - 1 > - 1 and nums[m] == nums[m-1]:
                if (m - l) % 2 == 0: #if the left side is an even size then there must be an element that only appears once there
                    r = m - 2
                else:
                    l = m + 1
            else:
                return nums[m]
            

class Solution2: #Alternative structure
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1

        while l <= r:
            m = (l + r)//2

            if (m-1 < 0 or nums[m] != nums[m-1]) and ( m+1 >= len(nums) or nums[m] != nums[m+1]):
                return nums[m]

            leftSize = m - 1 if nums[m] == nums[m-1] else m
            if leftSize % 2:
                r = m - 1
            else:
                l = m + 1
