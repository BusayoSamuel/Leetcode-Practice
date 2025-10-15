"""
https://leetcode.com/problems/best-team-with-no-conflicts/description/
"""


class Solution: #Time complexity O(n^2), Space complexity O(n^2)
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i], ages[i]] for i in range(len(scores))]
        pairs.sort()
        dp = {}

        def dfs(i, j):
            if i == len(pairs):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            mScore, mAge = pairs[j] if j >= 0 else [0, 0]
            score, age = pairs[i]
            res = 0
            if not (score > mScore and age < mAge):
                res = dfs(i + 1, i) + score  # add score
            dp[(i, j)] = max(res, dfs(i + 1, j))  # skip score
            return dp[(i, j)]

        return dfs(0, -1)

class Solution: #Same complexity as above
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i], ages[i]] for i in range(len(scores))]
        pairs.sort()
        dp = [pairs[i][0] for i in range(len(pairs))]

        for i in range(len(pairs)):
            mScore, mAge = pairs[i]
            for j in range(i):
                score, age = pairs[j]
                if mAge >= age:
                    dp[i] = max(dp[i], mScore + dp[j])

        return max(dp)
