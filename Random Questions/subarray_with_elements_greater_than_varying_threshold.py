"""
https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/description/
"""

class Solution: #Time complexity O(n), #Space complexity O(n)
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        left = [ i for i in range(n)]
        right = [ i for i in range(n)]
        
        #Finding the largest range in which nums[i] is the minimum
        stack = []
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                left[i] = left[stack.pop()]
            stack.append(i)


        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i] <= nums[stack[-1]]:
                right[i] = right[stack.pop()]
            stack.append(i)

        #if the minimum value is greater, then all the values in the range would be greater
        for i in range(n):
            k = right[i] - left[i] + 1
            if nums[i] > threshold/k:
                return k

        return -1
