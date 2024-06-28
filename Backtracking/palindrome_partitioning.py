"""
https://leetcode.com/problems/palindrome-partitioning/description/
"""

class MySolution: #Time complexity O(n*2^n), #Space complexity O(n*2^n) because there are 2^n possible partitions and it takes O(n) to check each one
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curSet = []

        def backtrack(i):
            if i >= len(s):
                res.append(curSet.copy())
                return

            #check for a palindrome in every substring starting from i
            for j in range(i, len(s)):
                l = i
                r = j

                isPali = True
                while l <= r:
                    if s[l] != s[r]:
                        isPali = False
                        break

                    l += 1
                    r -= 1
                    
                if isPali:
                    curSet.append(s[i:j+1])
                    backtrack(j+1)
                    curSet.pop()

        backtrack(0)
        return res


class CleanerSolution: #Same complexity
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
