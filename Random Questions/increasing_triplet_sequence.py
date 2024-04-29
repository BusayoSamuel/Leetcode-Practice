"""
https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=featured-list&envId=top-interview-questions
"""


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        maxRight = [0] * len(nums) #this array tells you the maximum number of the right of an index position
        maxRight[-1] = float("-inf")

        for i in range(len(nums)-2, -1, -1):
            maxRight[i] = max(maxRight[i+1], nums[i+1])

        minLeft = float("inf") #tells you lowest number encountered so far

        for i in range(len(nums)):
            if minLeft < nums[i] < maxRight[i]:
                return True

            minLeft = min(minLeft, nums[i])

        return False
    
class OptimalSolution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf") 

        for num in nums:
            if num <= first: #by having this we ensure that first is as small as possible
                first = num
            elif num <= second: #by having this we ensure that first < second or at least there's a value < second
                second = num
            else: #first < second < num
                return True

        return False