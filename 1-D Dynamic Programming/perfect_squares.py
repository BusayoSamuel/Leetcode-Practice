"""
https://leetcode.com/problems/perfect-squares/description/
"""

class Solution: #Time complexity O(n*n^1/2), Space complexity O(n)
    def numSquares(self, n: int) -> int:
        dp = [math.inf] * (n+1)
        dp[0] = 0

        for target in range(1, n + 1): 
        #we consider all numbers less than n which allows us to consider the shortest path to that target
            for s in range(1, target + 1): 
                square = s * s #we consider ever square number less than target
                if target - square < 0: #this means every other following square isnt worth considering
                    break
                dp[target] = min(dp[target], 1 + dp[target-square]) #we update with the min number of steps we can take towards this target 

        return dp[n] 
    
class AlternativeSolution: 
    def numSquares(self, n: int) -> int:
        def backtrack(root, target, curLen, minLen):
            if target == 0: #This indicates we have come to a possible path, so we update minLen
                return min(curLen, minLen)

            if root < 1 or curLen >= minLen: #The path we took isn't tenable or we've tried all possible roots, so we return minLen
                return minLen

            if root**2 <= target: #we try to minimise the length by taking a square step
                minLen = backtrack(root, target-(root**2), curLen + 1, minLen)

            #we consider the next smaller root
            minLen = backtrack(root - 1, target, curLen, minLen)
            return minLen

        return backtrack(int(math.sqrt(n)), n, 0, math.inf) #we start with largest possible perfect squ