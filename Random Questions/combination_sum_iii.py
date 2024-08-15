"""
https://leetcode.com/problems/combination-sum-iii/
"""

class MySolution: #Time complexity: O(1) due to a fixed number of loops(9) and max k can be is 9, Space complexity: O(k)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(i, curSum):
            nonlocal res
            nonlocal cur

            if curSum == n and len(cur) == k:
                res.append(cur.copy())
                return

            if curSum > n or i >= 10:
                return

            for j in range(i, 10):
                cur.append(j)
                backtrack(j+1, curSum + j)
                cur.pop()

        backtrack(1, 0)
        return res
