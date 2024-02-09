"""
https://leetcode.com/problems/optimal-division/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def optimalDivision(self, nums: List[int]) -> str: #the result is always maximised by minimising the denominator
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        else:
            return  str(nums[0]) + "/(" + "/".join(list(map(str, nums[1:]))) + ")"

