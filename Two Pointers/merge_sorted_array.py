"""
https://leetcode.com/problems/merge-sorted-array/submissions/1058955912/
"""

class Solution: #Time complexity 0(m+n), #Space complexity O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        l1 = 0
        l2 = 0
        r = m

        while l1 < m + n and l2 < n:
            if nums2[l2] <= nums1[l1]:
                temp = r
                while r != l1 and r < m + n:
                    nums1[r], nums1[r-1] = nums1[r-1], nums1[r]
                    r -= 1
                nums1[l1] = nums2[l2]
                r = temp + 1
                l2 += 1

            if nums1[l1] == 0 and l1 == r:
                nums1[l1] = nums2[l2]
                r += 1
                l2 += 1
            
            l1 += 1
        