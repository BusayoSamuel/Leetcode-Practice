"""
https://leetcode.com/problems/subarray-product-less-than-k/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        prod = 1
        res = 0

        for r in range(l, len(nums)):
            prod *= nums[r]

            while l <= r and prod >= k:
                prod /= nums[l]
                l += 1 #so if num[r] >= k, 0 is added to res

            res += (r-l+1) #adding all subbarrays that end at r

        return res


