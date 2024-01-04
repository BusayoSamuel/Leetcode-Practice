"""
https://leetcode.com/problems/counting-words-with-a-given-prefix/submissions/1135747551/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        l = 0
        r = len(pref)

        for i in range(len(words)):
            if words[i][l:r] == pref:  #doesn't matter if r is larger than len(words[i])
                count+=1

        return count
