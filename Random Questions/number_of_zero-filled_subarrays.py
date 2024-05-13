"""
https://leetcode.com/problems/number-of-zero-filled-subarrays/description/
"""

class MySolution: #Time complexity O(n^2), Space complexity O(1)
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            j = i
            while j < len(nums) and nums[j] == 0:
                count += 1
                j += 1

        return count
        


class OptimalSolution: #Time complexity O(n), Space complexity O(1)
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        i = 0

        while i < len(nums):
            j = i
            n = 0
            while i < len(nums) and nums[i] == 0:
                n += 1
                i += 1
            res += (n*(n+1))//2

            i += 1
            

        return res
        