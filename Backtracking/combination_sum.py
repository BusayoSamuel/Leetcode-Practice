"""
https://leetcode.com/problems/combination-sum/description/
"""

class Solution: #Time complexity O(2^target) because candidates can be 2 at the minimum which means you'd at least have target/2 size of array, Space complexity O(N) because each combination takes o(n) calls but combinations are made one after the other
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curSet = []

        def decide(idx, curSum):
            if curSum == target and curSet:
                res.append(curSet.copy())
                return #important to return at this point to avoid duplicates, you don't have to worry about any candidate element being zero

            if curSum > target or idx >= len(candidates):
                return

            curSum += candidates[idx]
            curSet.append(candidates[idx])
            decide(idx, curSum) # to allow for selecting an element multiple times
            curSet.pop()
            curSum -= candidates[idx]

            decide(idx + 1, curSum) #only consider elements in forward positions to avoid duplicates

        decide(0, 0)
        return res
 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

class MyOtherSolution: #Same complexity as above
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i, curTotal):
            if i >= len(candidates) or curTotal > target:
                return

            if curTotal == target:
                res.append(cur.copy())
                return

            for j in range(i, len(candidates)):
                cur.append(candidates[j])
                dfs(j, curTotal + candidates[j])
                cur.pop()

        dfs(0, 0)
        return res


