"""
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
"""

class Solution: #Time complexity O(mlongm) + O(nlogm) where m is size of potions and n is size of spells, Space complexity O(n)
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions = sorted(potions)

        for i in range(len(spells)):
            count = 0
            l = 0
            r = len(potions) - 1
            index = -1

            while l <= r:
                m = (r+l)//2

                if spells[i] * potions[m] >= success:
                    r = m - 1
                else:
                    index = max(index, m)
                    l = m + 1

            res.append(len(potions)-1-index)

        return res

        