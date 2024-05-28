"""
https://leetcode.com/problems/add-minimum-number-of-rungs/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def addRungs(self, rungs: List[int], dist: int) -> int:
        rungs = [0] + rungs
        res = 0

        for i in range(1, len(rungs)):
            res += (rungs[i] - rungs[i-1] - 1)//dist

        return res