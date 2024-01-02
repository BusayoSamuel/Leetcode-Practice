"""
https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/description/
"""

class Solution: 
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:

        gcd = 0
        for i in numsDivide:
            gcd = int(math.gcd(gcd,i))

        nums.sort()

        i = 0
        while i < len(nums):
            if gcd % nums[i] == 0:
                return i 
            else:
                curMin = nums[i]
                while i < len(nums) and nums[i] == curMin:
                    i += 1

        return -1