"""
https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description/
"""


class MySolution: #Time complexity O(n), Space complexity O(1)
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canShare(num):
            res = 0

            for pile in candies:
                res += pile // num
                if res >= k:
                    return True
            return False

        l = 1
        r = max(candies)
        res = 0

        while l <= r:
            m = (l+r)//2

            if canShare(m):
                res = m
                l = m + 1
            else:
                r = m - 1

        return res


      
            
