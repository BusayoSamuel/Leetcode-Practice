"""
https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(n)
    def maxScore(self, s: str) -> int:
        left = [0 for i in range(len(s)-1)]
        right = [0 for i in range(len(s)-1)]

        zeros = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros += 1

            left[i] = zeros

        ones = 0
        for i in range(len(s) - 2, -1, -1):
            if s[i+1] == "1":
                ones += 1

            right[i] = ones

        scores = [0 for i in range(len(s)-1)]
        for i in range(len(s)-1):
            scores[i] = left[i] + right[i]

        return max(scores)

class CleanerSolution: #Time complexity O(n), Space complexity O(1)
    def maxScore(self, s: str) -> int:
        zero = 0
        one = s.count("1")
        res = 0


        for i in range(len(s)-1):
            if s[i] == "0":
                zero += 1
            else:
                one -= 1

            res = max(res, zero + one)

        return res
        
