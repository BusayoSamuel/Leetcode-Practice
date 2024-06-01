"""
https://leetcode.com/problems/permutations-ii/description/
"""

class MySolution: #Time complexity O(n^n!), Space complexity O(n^n!)
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
        