"""
https://leetcode.com/problems/length-of-last-word/description/
"""

class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip() #O(n) time complexity

        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                return len(s[i+1:])

        return len(s)
    

class Solution2: #O(n) time complexity, #0(1) space complexity
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and count == 0:
                continue
            
            if s[i] == " ":
                return count
            count += 1

        return count

class Solution3:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split() #O(n) time complexity
        return len(words[-1])