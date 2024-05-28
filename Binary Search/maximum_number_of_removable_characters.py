"""
https://leetcode.com/problems/maximum-number-of-removable-characters/description/
"""
class Solution: #Time complexity O((n+k)logm), #Space complexity(k)  where n is len(s) and m is len(removable)
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

            removed = set(removable[:m+1]) #this will take O(k) time in the worst case

            if isSubseq():
                k = max(k, m + 1)
                l = m + 1
            else:
                r = m - 1 

        return k 


class MySolution: #Same complexity
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check(remidx):
            j = 0
            for i in range(len(s)):
                if i in remidx:
                    continue

                if p[j] == s[i]:
                    j += 1
                    if j >= len(p):
                        return True

            return False

        l = 0
        r = len(removable) - 1
        res = 0

        while l <= r:
            m = (r+l)//2

            if check(set(removable[:m+1])):
                res = m + 1
                l = m + 1
            else:
                r = m - 1

        return res

            
        
