"""
https://leetcode.com/problems/monotonic-array/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(1)
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = True
        decrease = True

        for i in range(len(nums)):
            if i > 0 and nums[i] > nums[i-1]:
                decrease = False
                break

        for i in range(len(nums)):
            if i > 0 and nums[i] < nums[i-1]:
                increase = False
                break

        return increase or decrease

class CleanerSolution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increase = True
        decrease = True

        for i in range(len(nums)):
            if i > 0 and nums[i] > nums[i-1]:
                decrease = False
                
            if i > 0 and nums[i] < nums[i-1]:
                increase = False

        return increase or decrease
