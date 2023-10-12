"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
"""


class Solution: #Time complexity O(nlogm) where m is the sum of weights, Space complexity O(1)
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,  r = max(weights), sum(weights) #the lower bound would be the largest weight and the upper bound is the sum of all weight
        res = r

        def canShip(cap): #returns the number of ships needed for this capacity
            ships, currCap = 1, cap  
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap -= w
            return ships <= days #if the more ships are needed than days then the cap is too low

        while l <= r:
            m = (l+r)//2

            if canShip(m):
                r = m - 1
                res = min(m, res)
            else:
                l = m + 1 #cap is too low so we increment the lower bound

        return res
        