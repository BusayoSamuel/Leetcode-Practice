"""
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
"""

class MySolution: #Time complexity O(n^2), Space complexity O(n)
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()

        for i, c in enumerate(s):
            right = set(s[i+1:])

            for j in range(0, i):
                if s[j] in right:
                    res.add(s[j]+s[i]+s[j])


        return len(res)

class Solution: #Time complexity O(26n), Space complexity O(n)
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = collections.Counter(s)
        
        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            
            for j in range(26):
                c = chr(ord('a') + j)
                if c in left and c in right:
                    res.add((s[i], c))
            left.add(s[i])
            
        return len(res)
