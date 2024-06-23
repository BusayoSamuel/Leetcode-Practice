"""
https://leetcode.com/problems/assign-cookies/
"""

class MySolution: #Time complexity O(nlogn), Space complexity O(n) due to sorting
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        i = 0
        j = 0

        while j < len(s) and i < len(g):
            if s[j] >= g[i]:
                i += 1
                j += 1
            else:
                j += 1

        return i
