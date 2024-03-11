"""
https://leetcode.com/problems/n-th-tribonacci-number/description/
"""

class Solution: #Time complexity O(n), #Space complexity O(1)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            T0 = 0
            T1 = 1
            T2 = 1
            cur = 0
            for i in range(2, n):
                cur = T0 + T1 + T2

                T0 = T1
                T1 = T2
                T2 = cur

            return cur