"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

class Solution: #Time complexity O(logn), Space complexity O(1)
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = 5000

        while l <= r:
            if nums[l] < nums[r]: #takes care of a scenario where the array is isn't rotated 
                res = min(res, nums[l])
                break

            m = (r + l)//2
            res = min(res, nums[m])
            if  nums[m] < nums[l]: #this means the lower sorted half is to the right
                r = m - 1
            else: 
                l = m + 1

        return res


class MySolution: #Same complexity
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (r+l)//2


            if nums[m] > nums[-1]: # this means the first half sorted portion is to the right
                l = m + 1 
            else: # now we're in the first half sorted portion
                if m > 0 and m < len(nums) - 1 and nums[m-1] < nums[m] < nums[m+1]: #if m == 0 or len(nums)-1 or the left neighbour > right neighbour then it has to be the lowest number 
                    r = m - 1
                else:
                    return nums[m]
