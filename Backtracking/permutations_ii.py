"""
https://leetcode.com/problems/permutations-ii/description/
"""

class MySolution: #Time complexity O(nlogn), Space complexity O(n)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curSet = []
        nums.sort()
        
        def backtrack(numbers):
            if len(curSet) == len(nums):
                res.append(curSet.copy())
                return

            for idx, number in enumerate(numbers):
                if idx > 0 and numbers[idx] == numbers[idx-1]:
                    continue

                curSet.append(number)
                backtrack(numbers[:idx] + numbers[idx+1:])
                curSet.pop()

        backtrack(nums)
        return res

class MyOtherSolution: #Time complexity O(nlogn) due to sorting and nlogn > n!, Space complexity O(n)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        cur = []
        res = []
        picked = set()
        nums.sort()

        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for j in range(len(nums)):
                if j in picked or (j > 0 and nums[j] == nums[j-1] and j - 1 not in picked):
                    continue

                cur.append(nums[j])
                picked.add(j)
                dfs()
                cur.pop()
                picked.remove(j)


        dfs()
        return res
        

        
