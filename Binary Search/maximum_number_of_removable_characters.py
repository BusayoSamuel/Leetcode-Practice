"""
https://leetcode.com/problems/maximum-number-of-removable-characters/description/
"""
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        k = 0

        def isSubseq():
            j = 0

            for i in range(len(s)):
                if i not in removed and j < len(p) and s[i] == p[j]:
                    j += 1
                
            return j >= len(p)

        l , r = 0, len(removable) - 1

        while l<=r:
            m = (l+r)//2

            removed = set(removable[:m+1])

            if isSubseq():
                k = max(k, m + 1)
                l = m + 1
            else:
                r = m - 1 

        return k 