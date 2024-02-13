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


class InefficientSolution: #Time complexiy O(n^2), Space complexity O(n)
    def minOperations(self, nums: List[int], x: int) -> int:
        prefix = [] #sum of nums from the left
        postfix = [] #sum of nums from the right
        curSum = 0
        res = len(nums) + 1

        for i in range(len(nums)):
            curSum += nums[i]
            prefix.append(curSum)

        curSum = 0

        for j in range(len(nums)-1, -1, -1): 
            curSum += nums[j]
            postfix = [curSum] + postfix

        for i in range(len(nums)):
            if prefix[i] == x: #checking if the the prefix on its own would meet the target
                res = min(res, i + 1)
            for j in range(i, len(nums)):
                if prefix[i] + postfix[j] == x:
                    res = min(res, i + (-j + len(nums)) + 1)
                if postfix[j] == x:  #checking if the the postfix on its own would meet the target
                    res = min(res, -j + len(nums))

        return res if res != len(nums) + 1 else -1
