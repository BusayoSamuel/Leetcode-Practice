"""
https://leetcode.com/problems/arranging-coins/description/
"""
import math
class Solution: #0(n) time complexity, #O(1) space complexity
    def arrangeCoins(self, n: int) -> int:
        take = 1
        count = 0

        while take <= n:
            n -= take
            count += 1
            take += 1

        return count
    

class Solution:  #O(logn) time complexity, #O(1) space complexity
    def arrangeCoins(self, n: int) -> int:
        l = 1 #least number of possible complete rows
        r = n #n serves as an upper bound to the number of complete rows e.g if n = 1
        res = 1

        while l <= r:
            m = (l + r)//2
            need = m/2*(m+1) #tells you the number of coins needed to fill m rows

            if need > n:
                r = m - 1
            elif need < n:
                res = max(res, m)
                l = m + 1            
            else:
                return m

        return res
    
class Solution: #O(1) time complexity, #0(1) space complexity
    def arrangeCoins(self, n: int) -> int:
        #r/2(r+1) = n so, r^2 + r - 2n = 0 where r = number of rows
        a = 1
        b = 1
        c = -2 * n

        r = (-1 + math.sqrt(1 - (4*c)))/2  #solving the quadratic equation
        return math.floor(r) #rounding down