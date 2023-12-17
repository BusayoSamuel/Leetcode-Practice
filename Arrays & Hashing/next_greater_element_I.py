"""
https://leetcode.com/problems/next-greater-element-i/description/
"""

class Solution1: #Time complexity O(n^2), Space complexity O(n)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    ans.append(-1)
                    k = j + 1
                    while k < len(nums2):
                        if nums1[i] < nums2[k]:
                            ans[-1] = nums2[k]
                            break
                        k += 1
                    break

        return ans