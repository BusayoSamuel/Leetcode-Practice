"""
https://leetcode.com/problems/intersection-of-two-arrays/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(n)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset = set()
        nums1 = set(nums1)

        for num in nums2:
            if num in nums1:
                hashset.add(num)

        return list(hashset)

class OtherSolution: #Time complexity O(nlogn), Space complexity O(n) due to sorting
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j, N, M = 0, 0, len(nums1), len(nums2)
        res = []

        while i < N and j < M:
            while j < M and nums2[j] < nums1[i]:
                j += 1

            if j < M:
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
                i += 1
                while i < N and nums1[i] == nums1[i-1]:
                    i += 1

        return res


        
