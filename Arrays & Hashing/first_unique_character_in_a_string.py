"""
https://leetcode.com/problems/first-unique-character-in-a-string/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(n)
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)

        for i, c in enumerate(s):
            if counts[c] == 1:
                return i

        return -1

class MyOtherSolution: #Time complexity O(n), Space complexity O(n)
    def firstUniqChar(self, s: str) -> int:
        counts = {}

        for c in s:
            counts[c] = counts.get(c,0) + 1

        for i, c in enumerate(s):
            if counts[c] == 1:
                return i

        return -1
        
        
