"""
https://leetcode.com/problems/minimum-window-substring/description/
"""

class Solution: #Time complexity O(n+m), Space complexity O(n+m)
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        countCur = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res, resLen = [-1, -1], math.inf
        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
            if s[r] in countT:
                countCur[s[r]] = 1 + countCur.get(s[r], 0)
                if countCur[s[r]] == countT[s[r]]:
                    have += 1

            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1

                if s[l] in countT:
                    countCur[s[l]] -= 1
                    if countCur[s[l]] < countT[s[l]]:
                        have -= 1
                
                l += 1

        l, r = res

        return s[l:r+1] if resLen < math.inf else ""

            
