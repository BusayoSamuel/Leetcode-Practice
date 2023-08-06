"""
https://leetcode.com/problems/valid-anagram/description/
"""

class Solution1: #O(n) time complexity, #O(1) space complexity because there are only 26 lowercase letters
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i], 0)

        for i in range(len(t)):
            if t[i] not in counts:
                return False
            counts[t[i]] -= 1

        for i in counts.values():
            if i != 0:
                return False
        
        return True
    

class Solution2: #O(n) time complexity, #O(1) space complexity because there are only 26 lowercase letters
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        count = [0] * 26

        for i in s:
            print(ord(i)-ord('a'))
            count[ord(i) - ord('a')] += 1

        for j in t:
            count[ord(j) - ord("a")] -= 1

        for k in count:
            if k: return False
        return True