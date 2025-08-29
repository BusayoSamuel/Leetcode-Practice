"""
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/description/
"""

class Solution: #Time complexity O(4^n), Space complexity O(2^n)
    def maxProduct(self, s: str) -> int:
        def isPal(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        N, pali = len(s), {}

        for mask in range(1, 1 << N):
            subseq = ""
            for i in range(N):
                if mask & (1 << i):
                    subseq += s[i]

            if isPal(subseq):
                pali[mask] = len(subseq)

        res = 0
        for m1 in pali:
            for m2 in pali:
                if m1 & m2 == 0:
                    res = max(res, pali[m1] * pali[m2])

        return res
