"""
https://leetcode.com/problems/create-target-array-in-the-given-order/description/
"""

class Solution: #Time complexity O(n^2), Space complexity O(n)
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:#
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])

        return target

class Solution: #Time complexity O(n^2), Space complexity O(n)
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target =[]
        for i in range(len(nums)):
                target = target[:index[i]] + [nums[i]] + target[index[i]:]
        return target


class ProbablyBestSolution: #Same complexity
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        def insert(arr, ind, val):
            new_arr = ["x"]*(len(arr) + 1)  #Initialise with required extra space.
            for i in range(0, ind):  #Fill up to insertion point.
                new_arr[i] = arr[i]
            new_arr[ind] = val #Insert our value.
            for i in range(ind + 1, len(new_arr)): #Fill remaining values, shifted.
                new_arr[i] = arr[i-1]
            return new_arr #Return new array.
            
        res = []
        for i in range(len(nums)):
            res = insert(res, index[i], nums[i])
        return res