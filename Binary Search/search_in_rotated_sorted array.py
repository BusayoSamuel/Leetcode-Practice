"""
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""

class Solution1: #Time complexity O(logn), Space complexity O(1)
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        def binarySearch(l, r):
            while l <= r:  

                m = (r + l)//2

                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    return m 
            
            return -1

        while l <= r:
            m = (r+l)//2

            if nums[m] >= nums[l]: #this means we are in the left sorted ported
                if target <= nums[m] and target >= nums[l]:
                    return binarySearch(l, m) #This means the range of numbers betweem l and m are sorted
                else: #search right
                    l = m + 1
            elif nums[m] <= nums[r]: #this means we are in the right sorted ported
                if target >= nums[m] and target <= nums[r]: #This means the range of numbers betweem m and r are sorted
                    return binarySearch(m, r)
                else:
                   r = m - 1 #search left
                

        return -1


class Solution2: #Same complexity but much cleaner
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m

            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1
        