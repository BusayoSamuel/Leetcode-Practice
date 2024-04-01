"""
https://leetcode.com/problems/power-of-two/description/
"""

class Solution: #Time complexity O(logn), Space complexity O(1)
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1:
            n /= 2

        return n == 1 if n != 1 else True
        

class OptimalSolution: #Time complexity O(1), Space complexity O(1)
    def isPowerOfTwo(self, n: int) -> bool:
        #bit manipulation, powers of 2 always have leading 1 with trailing zeros(i.e 1000...), so if subtract 1 you get 11111... and if you AND those two values you get zero
        return n > 0 and n & (n-1) == 0 
        