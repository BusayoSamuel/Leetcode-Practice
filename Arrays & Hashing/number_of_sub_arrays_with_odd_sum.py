"""
https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur = 0
        odd = 0
        even = 0
        res = 0
        
        for r in range(len(arr)):
            cur += arr[r]

            if cur % 2 == 0:
                even += 1
                res += odd
            else:
                odd += 1
                res += even + 1

        return res % (10**9 + 7)
