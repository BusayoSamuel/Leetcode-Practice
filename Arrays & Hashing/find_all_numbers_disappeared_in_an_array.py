"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
"""


class Solution: #Time complexity O(n), Space complexity O(N)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        fullList = { i for i in range(1, len(nums)+1)}
        for i in range(len(nums)):
            if nums[i] in fullList:
                fullList.remove(nums[i])

        return list(fullList)
    
class BetterSolution: #Time complexity O(n), Space complexity O(1)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)): #in this loop, we map values that exist, by using them as indexes
            idx = abs(nums[i])
            nums[idx - 1] = -abs(nums[idx-1])

        for i in range(len(nums)): #so if the value is negative, we know what index number needs to be added to the res list
            if nums[i] > 0:
                res.append(i+1)

        return res