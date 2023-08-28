"""
https://leetcode.com/problems/merge-strings-alternately/description/
"""

class Solution1: #0(n) time complexity, #O(n) space complexity
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        lower = word1 if len(word1) < len(word2) else word2
        higher = word1 if len(word1) > len(word2) else word2

        for i in range(len(lower)):
            res.append(word1[i])
            res.append(word2[i])

        res.append(higher[i+1:])

        return "".join(res)


class Solution2: #Alternative Structure
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j, res = 0, 0, []

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)