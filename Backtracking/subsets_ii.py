"""
https://leetcode.com/problems/subsets-ii/description/
"""

class Solution: #Time complexity O(n*2^n), Space complexity O(n*2^n)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curSet = []

        def backtrack(i):
            if i == len(nums):
                res.append(curSet.copy()) #only append after you've considered all options
                return

            curSet.append(nums[i])
            backtrack(i + 1)
            last = curSet.pop() #we reference the last item that was added to avoid duplicates

            while i + 1 < len(nums) and last == nums[i+1]:
                i += 1

            backtrack(i + 1)

        backtrack(0) 
        return res