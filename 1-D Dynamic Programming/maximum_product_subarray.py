"""
https://leetcode.com/problems/maximum-product-subarray/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) 
        curMax, curMin = 1, 1 #keep track of the min and max value as we iterate through the array

        for n in nums:
            tmp = curMax * n #in case curMax is updated in the next line
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp, curMin * n, n)
            res = max(res, curMax)

        return res
