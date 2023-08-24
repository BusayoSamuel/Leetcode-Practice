"""
https://leetcode.com/problems/valid-perfect-square/description/
"""

class Solution: #O(logn) time complexity, #O(1) space complexity
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num

        while l <= r:
            m = (l+r)//2
            sq = m ** 2

            if sq > num:
                r = m - 1
            elif sq < num:
                l = m + 1
            else:
                return True

        return False
    
