"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        l = 0
        curSum = 0
        maxW = -1 #maxW refers to the max window thats left behind after the operations

        for r in range(len(nums)):
            curSum += nums[r]

            while l <= r and curSum > target:
                curSum -= nums[l]
                l += 1

            if curSum == target: #Checking for target last is important to catch valid window at the edge of the array
                maxW = max(maxW, r-l+1)

        return -1 if maxW == -1 else len(nums) - maxW