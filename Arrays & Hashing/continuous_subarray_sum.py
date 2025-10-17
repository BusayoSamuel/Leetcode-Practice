"""
https://leetcode.com/problems/continuous-subarray-sum/description/
"""

class MyInefficientSolution: #Time complexity O(n^2), Space complexity O(1)
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        if k == 1:
            return True 

        for i in range(1, len(nums)):
            curSum = sum(nums[:i])
            l = 0
            for j in range(i, len(nums)):
                curSum += nums[j]
                while j > l and j - l + 1 > i + 1:
                    curSum -= nums[l]
                    l += 1

                if curSum % k == 0 or curSum == 0:
                    return True

        return False


class Solution: #Time complexity O(n), Space complexity O(k)
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}  # remainder -> end index
        total = 0

        for i, num in enumerate(nums):
            total += num
            r = total % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True

        return False


        
