"""
https://leetcode.com/problems/fruit-into-baskets/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def totalFruit(self, fruits: List[int]) -> int:
        counts = {}
        l = 0
        res = 0
        
        for r in range(len(fruits)):
            counts[fruits[r]] = 1 + counts.get(fruits[r], 0)
            
            while len(counts.keys()) > 2:
                counts[fruits[l]] -= 1
                if counts[fruits[l]] == 0:
                    del counts[fruits[l]]
                l += 1

            res = max(res, r-l+1)

        return res


class MySolution: #Same complexity as above
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        res = 0
        hashmap = defaultdict(int)

        for r in range(len(fruits)):
            hashmap[fruits[r]] += 1
            while len(hashmap) > 2:
                hashmap[fruits[l]] -= 1
                if hashmap[fruits[l]] == 0:
                    hashmap.pop(fruits[l])
                l += 1

            res = max(res, r - l + 1)

        return res

            

        
        
