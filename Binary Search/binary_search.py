"""
https://leetcode.com/problems/binary-search/description/

"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r: # "<=" covers cases where the list contains a single item
            m = (l + r)//2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
            
        return -1
