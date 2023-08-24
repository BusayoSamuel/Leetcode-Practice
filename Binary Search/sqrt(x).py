"""
https://leetcode.com/problems/sqrtx/description/
"""

class Solution: #O(logn) time complexity, #O(1) space complexity 
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0

        while l <= r:
            m = (l + r)//2
            sq = m * m

            if sq > x:
                r = m - 1
            elif sq < x:
                res = max(res, m)
                l = m + 1
            else:
                return m

        return res 