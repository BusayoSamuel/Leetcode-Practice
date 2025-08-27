"""
https://leetcode.com/problems/solving-questions-with-brainpower/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(n)
    def mostPoints(self, questions: List[List[int]]) -> int:
        res = [0] * (len(questions) + 1)
        for i in range(len(questions)-1, -1, -1):
            maxPoint = 0
            skip = 0
            maxPoint = max(maxPoint, skip + res[i+1])
            choose = questions[i][0]
            maxPoint = max(maxPoint, choose)
            if (i + questions[i][1] + 1) < len(questions):
                maxPoint = max(maxPoint, choose + res[i + questions[i][1] + 1])
            
            res[i] = maxPoint
        return res[0] 

class CleanerSolution: #Same complexity as above
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = {}

        for i in range(len(questions) - 1, -1, -1):
            dp[i] = max(
                questions[i][0] + dp.get(i + 1 + questions[i][1], 0),
                dp.get(i + 1, 0)
            )
        return dp.get(0)
        
        
