"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
"""

class Solution: #Time complexity O(logn), Space complexity O(1)
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (r+l)//2

            if m == 0 or arr[m-1] < arr[m] < arr[m+1]:
                l = m + 1
            elif m == len(arr) - 1 or  arr[m-1] > arr[m] > arr[m + 1]:
                r = m - 1
            else:
                return m