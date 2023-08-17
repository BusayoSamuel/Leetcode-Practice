"""
https://leetcode.com/problems/squares-of-a-sorted-array/description/
"""
class Solution: # O(n) time complexity, #O(n) space complexity
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        res = []

        while l <= r: #adding the largest square to the end of the res array 
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l]**2)
                l += 1
            else:
                res.append(nums[r]**2)
                r -= 1
        
        return res[::-1] #reversing the order of the list. O(n) time complexity
