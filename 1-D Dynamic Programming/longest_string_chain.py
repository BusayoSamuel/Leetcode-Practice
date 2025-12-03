"""
https://leetcode.com/problems/longest-string-chain/
"""

class MySolution: #Time complexity O(n*m^2), Space complexity O(n)
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x : len(x) )
        dp = [1] * len(words) 

        def isValid(word1, word2):
            i = 0
            j = 0

            inserts = 1

            while i < len(word1):
                if word1[i] != word2[j]:
                    if inserts:
                        j += 1
                        inserts -= 1
                        continue
                    else:
                        return False

                i += 1
                j += 1
            
            return True

        for i in range(len(words)-2, -1, -1):
            for j in range(i, len(words)):
                if len(words[i]) + 1 == len(words[j]) and isValid(words[i], words[j]):
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


class OtherSolution: #Same complexity as above
    def longestStrChain(self, words: List[str]) -> int:
        def isPred(w1, w2):
            i = 0
            for c in w2:
                if i == len(w1):
                    return True
                if w1[i] == c:
                    i += 1
            return i == len(w1)

        words.sort(key=len)
        n = len(words)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if len(words[j]) + 1 < len(words[i]):
                    break
                if len(words[j]) + 1 > len(words[i]) or not isPred(words[j], words[i]):
                    continue
                dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


