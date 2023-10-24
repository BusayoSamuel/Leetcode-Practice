"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        currSum = 0
        res = float("Inf")

        while currSum < target and r < len(nums):
            currSum += nums[r]
            

            while currSum >= target:
                res = min(res, r - l + 1)
                currSum -= nums[l]
                l+=1


            r += 1

        return 0 if res == float("Inf") else res

        