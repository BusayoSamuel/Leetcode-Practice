"""
https://leetcode.com/problems/range-sum-query-immutable/description/
"""

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int: #Time complexity O(n), #Spaxe complexity O(1)
        return sum(self.nums[left:right+1])

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)