"""
https://leetcode.com/problems/subsets-ii/description/
"""

class Solution: #Time complexity O(nlogn + 2^n) due to sorting and backtracking, Space complexity O(n + 2^n) due to cur storing all nums and res storing all possible subsets
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #must be sorted to cut out any duplicates
        res = []
        curSet = []

        def backtrack(i):
            if i == len(nums):
                res.append(curSet.copy()) #only append after you've considered all options
                return

            curSet.append(nums[i])
            backtrack(i + 1)
            last = curSet.pop() #we reference the last item that was added to avoid duplicates

            while i + 1 < len(nums) and last == nums[i+1]: #or use nums[i] instead of last
                i += 1

            backtrack(i + 1)

        backtrack(0) 
        return res
