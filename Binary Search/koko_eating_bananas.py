"""
https://leetcode.com/problems/koko-eating-bananas/
"""

class Solution: #Time complexity O(nlogmax(n)), Space complexity O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def howlong(k):
            count = 0

            for i in range(len(piles)):
                count += math.ceil(piles[i]/k)

            return count 

        l = 1
        r = max(piles)

        res = r

        while l <= r:
            k = (r+l)//2

            if howlong(k) > h:
                l = k + 1
            else:
                r = k - 1
                res = min(res, k)


        return res