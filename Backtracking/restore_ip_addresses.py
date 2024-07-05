"""
https://leetcode.com/problems/restore-ip-addresses/description/
"""

class MySolution: #Time complexity O(3^4), Space complexity O(3^4) because at most we're gonna consider strings up to a len of 3 for each of the 4 integers
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        cur = []
        def backtrack(i):
            if len(cur) == 4:
                if i >= len(s):
                    res.append(".".join(cur))
                return

            for j in range(i + 1, len(s) + 1): #we go up to len(s) + 1 to ensure that we enter then base case at the top
                if j - i > 1 and s[i] == "0":
                    return

                if not 0 <= int(s[i:j]) <= 255: # thereby the length of s[i:j] would never be greater than 3
                    return

                cur.append(s[i:j])
                backtrack(j)
                cur.pop()

        backtrack(0)
        return res


class OtherSolution: #Same complexity
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        if len(s) > 12:
            return res

        def backtrack(i, dots, curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1]) #the -1 is to get rid of the last dot
                return

            if dots > 4:
                return

            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(j + 1, dots + 1, curIP + s[i:j+1] + ".")
                  
        backtrack(0, 0, "")
        return res
        
        
