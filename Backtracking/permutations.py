"""
https://leetcode.com/problems/permutations/description/
"""

class MySolution: #Time complexity O(n! * n) because there are n! permutations and creating a copy takes O(n) time, Space complexity(n!)
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curSet = []
        q = deque(nums)

        def backtrack(q):
            if len(curSet) == len(nums):
                res.append(curSet.copy())
                return

            for i in range(len(q)):
                num = q.popleft()
                curSet.append(num)
                backtrack(q)
                q.append(num)
                curSet.pop()

        backtrack(q)
        return res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # base case
        if len(nums) == 1:
            return [nums[:]]  # nums[:] is a deep copy

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res


class MyOtherSolution: #Same complexity
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        picked = set()


        def dfs():
            if len(nums) == len(picked):
                res.append(cur.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in picked:
                    cur.append(nums[i])
                    picked.add(nums[i])
                    dfs()
                    cur.pop()
                    picked.remove(nums[i])

        dfs() 
        return res
        
