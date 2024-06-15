"""
https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/
"""

class MySolution: #Time complexity O(2^n), Space complexity O(2^n)
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        curSet = []

        def backtrack(i, total):
            nonlocal res

            if i >= len(nums):
                res += total
                return

            curSet.append(nums[i])
            backtrack(i+1, total ^ nums[i])
            curSet.pop()

            backtrack(i+1, total)

        backtrack(0, 0)
        return res
    
class CleanerSolution: #Same complexity
    def subsetXORSum(self, nums: List[int]) -> int:

        def backtrack(i, total):

            if i >= len(nums):
                return total

            return backtrack(i+1, total ^ nums[i]) + backtrack(i+1, total)

        return backtrack(0, 0)
    
class EfficientSolution: #Time complexity O(n), Space complexity O(1)
    def subsetXORSum(self, nums: List[int]) -> int:
        
        total = 0
        for num in nums:
            total |= num

        return total * (2**(len(nums)-1))

