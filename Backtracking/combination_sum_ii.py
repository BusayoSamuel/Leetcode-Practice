"""
https://leetcode.com/problems/combination-sum-ii/description/
"""

class MySolution: #Time complexity O(2^n), Space complexity O(n)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        subset = []

        def backtrack(i, subtarget): 
            if subtarget == 0:
                res.append(subset.copy())

            if i >= len(candidates) or subtarget < 0:
                return

            if candidates[i] <= subtarget:
                subset.append(candidates[i])
                backtrack(i+1, subtarget - candidates[i]) 
                subset.pop()

                while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                    i += 1

                backtrack(i + 1, subtarget)

        backtrack(0, target)
        return res
    

class OtherSolution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res

class MyOtherSolution: #Same complexity
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cur = []
        res = []
        candidates.sort()

        def dfs(i, curSum):
            if curSum == target:
                res.append(cur.copy())

            if i >= len(candidates) or curSum > target:
                return

            for j in range(i, len(candidates)):
                if j == i or candidates[j] != candidates[j - 1]:
                    cur.append(candidates[j])
                    dfs(j+1, curSum + candidates[j])
                    cur.pop()

        dfs(0, 0)
        return res

        
