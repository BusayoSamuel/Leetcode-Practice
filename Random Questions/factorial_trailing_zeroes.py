"""
https://leetcode.com/problems/factorial-trailing-zeroes/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def trailingZeroes(self, n: int) -> int:
        fact = 1

        while n:
            fact *= n
            n -= 1

        res = 0

        while fact % 10 == 0:
            res += 1
            fact = fact // 10

        return res


class BetterSolution: #Time complexity O(logn), Space complexity O(1)
    def trailingZeroes(self, n: int) -> int: #The number of trailing zeros is determined by the number of times you multiply by a multiple of 5
        cnt = 0

        while n != 0: 
            n = n // 5 #This tells you the multiple of 5s you can find in n, and subsequently the number of 25s and so on
            cnt += n

        return cnt