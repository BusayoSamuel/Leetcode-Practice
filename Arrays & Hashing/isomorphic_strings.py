"""
https://leetcode.com/problems/isomorphic-strings/description/
"""

class Solution1:#Time complexity O(n), Space complexity O(n)
    def isIsomorphic(self, s: str, t: str) -> bool:
        pairs = {}

        for i in range(len(s)):
            if s[i] not in pairs:
                if t[i] in set(pairs.values()):
                    return False
                pairs[s[i]] = t[i] 

            if pairs[s[i]] != t[i]:
                return False
        
        return True

class Solution2: #Same time complexity
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):
            if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1

        return True