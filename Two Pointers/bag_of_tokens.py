"""
https://leetcode.com/problems/bag-of-tokens/submissions/1494864761/
"""

class MySolution: #Time complexity O(nlogn), Space complexity O(n) due to sorting
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens)-1
        res = 0
        score = 0

        if not tokens or power < tokens[l]:
            return 0

        while l <= r:
            while score > 0 and l <= r and power < tokens[r]:
                power += tokens[r]
                score -= 1
                r -= 1

            while l <= r and power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1

            res = max(res, score)

        return res

class CleanerSolution: #Same complexity as above
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        l = 0
        r = len(tokens)-1
        res = 0
        score = 0
        tokens.sort()

        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                res = max(res, score)
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break

        return res

            
