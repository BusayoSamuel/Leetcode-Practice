"""
https://leetcode.com/problems/132-pattern/description/
"""

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] #integer, MinLeft #montonically decreasing
        curMin = nums[0]

        for k in range(1, len(nums)): #keeps track of the k value
            while stack and nums[k] >= stack[-1][0]: #stack[-1][0] is selected as j if nums[k] < nums[j]
                stack.pop()
            if stack and nums[k] > stack[-1][1]: #stack[-1][1] is the minimum value to the left, so it can be claimed as i if nums[k] > nums[i]
                return True

            stack.append([nums[k], curMin])
            curMin = min(curMin, nums[k]) #keep track of curMinimum to the left

        return False