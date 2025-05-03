"""
https://leetcode.com/problems/word-break/description/
"""

class Solution: #Time complexity O(n^2), Space complexity O(1)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = {}

        def backtrack(i):
            if i in dp:
                return dp[i]

            if i >= len(s):
                return True

            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    dp[j+1] = backtrack(j+1)
                    if dp[j+1]:
                        return True

            return False

        return backtrack(0) 

class Solution: #Time complexity O(n*m*k), Space complexity O(1) where n is the length of s, m is the number of words, and k is the length of the longest word
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):
            for word in wordDict: #compare each word in the dictionary 
                if (i + len(word) <= len(s)) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                if dp[i]:
                    break
            
        return dp[0]

        
