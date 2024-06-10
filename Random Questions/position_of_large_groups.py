"""
https://leetcode.com/problems/positions-of-large-groups/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(n)
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        l = 0
        res = []

        for r in range(len(s)):
            if r == len(s) - 1 or s[l] != s[r + 1]:
                if r - l + 1 >= 3:
                    res.append([l, r])
                l = r + 1

        return res
        
