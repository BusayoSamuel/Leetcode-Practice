"""
https://leetcode.com/problems/find-pivot-index/description/
"""

class Solution1: #Time complexity O(n), Space complexity O(n)
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = []
        rightSum = []
        curSum = 0

        for i in range(len(nums)):
            leftSum.append(curSum)
            curSum += nums[i]

        curSum = 0

        for j in range(len(nums)-1, -1, -1):
            rightSum.append(curSum)
            curSum += nums[j]

        rightSum = rightSum[::-1]

        print(leftSum)
        print(rightSum)

        for k in range(len(nums)):
            if leftSum[k] == rightSum[k]:
                return k

        return -1
    

#More efficient solution
class Solution2: #Time complexity O(n), #Space complexity O(1)
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = []
        rightSum = []
        total = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]

        return -1