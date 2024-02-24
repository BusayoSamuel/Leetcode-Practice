"""
https://leetcode.com/problems/maximum-subarray/description/
"""

class Solution: #Time complexity O(n), Space compleity O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        cur = 0

        for num in nums:
            cur += num

            res = max(res, cur)

            cur = max(cur, 0) #The max subarray would always need to start with a positive number, 
			      #	adding negative numbers together offers no increase and they are best compared
			      # on their own

        return res

class DivideAndConquerSolution: #Time complexity O(nlogn), Space complexity O(logn)
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        mid = len(nums) //2
        left_max = self.maxSubArray(nums[:mid])
        right_max = self.maxSubArray(nums[mid:])

        left_cross = float("-inf")
        total = 0
        for i in range(mid - 1, -1, -1):
            total += nums[i]
            left_cross = max(left_cross, total)

        right_cross = float("-inf")
        total = 0
        for j in range(mid, len(nums)):
            total += nums[j]
            right_cross = max(right_cross, total)

        cross_max = left_cross + right_cross #finds the max sum that cuts across the left and right

        return max(left_max, right_max, cross_max)