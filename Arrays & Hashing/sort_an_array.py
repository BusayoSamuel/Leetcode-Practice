"""
https://leetcode.com/problems/sort-an-array/description/
"""

class Solution: #Time complexity O(nlogn), Space complexity O(n)
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        p1 = 0
        p2 = 0
        sortList = []

        while p1 < len(left) and p2 < len(right):
            if left[p1] <= right[p2]:
                sortList.append(left[p1])
                p1 += 1
            else:
                sortList.append(right[p2])
                p2 += 1

        if p1 < len(left):
            sortList += left[p1:]
        
        if  p2 < len(right):
            sortList += right[p2:]

        return sortList


        