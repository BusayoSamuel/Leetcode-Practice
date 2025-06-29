"""
https://leetcode.com/problems/get-equal-substrings-within-budget/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        cost = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] != t[r]:
                cost += abs(ord(s[r]) - ord(t[r]))

            while cost > maxCost:
                if s[l] != t[l]:
                    cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            res = max(r-l+1, res)

        return res


class MySolution: #Time complexity O(n), Space complexity O(1)
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0
        cost = 0
        l = 0
        
        for r in range(len(s)):
            cost += abs(ord(s[r])-ord(t[r]))

            while cost > maxCost:
                cost -= abs(ord(s[l])-ord(t[l]))
                l += 1

            res = max(res, r-l+1)

        return res


        

        
