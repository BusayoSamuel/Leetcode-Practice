"""
https://leetcode.com/problems/count-substrings-starting-and-ending-with-given-character/description/
"""

class MyInitialSolution: #Time complexity O(n^2), Space complexity O(1)
    def countSubstrings(self, s: str, c: str) -> int:
        res = 0
        for i in range(len(s)):
            if s[i] != c:
                continue

            for j in range(i, len(s)):
                if s[j] == c:
                    res += 1

        return res

class MyEfficientSolution: #Time complexity O(n), Space complexity O(1)
    def countSubstrings(self, s: str, c: str) -> int:
        count = 0
        res = 0
        for i in range(len(s)):
            if s[i] == c:
                count += 1

        while count:
            res += count
            count -= 1

        return res

class MyCleanerSolution: #Same complexity
    def countSubstrings(self, s: str, c: str) -> int:
        count = 0
        res = 0
        for i in range(len(s)):
            if s[i] == c:
                count += 1
                res += count

        return res
