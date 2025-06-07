"""
https://leetcode.com/problems/longest-increasing-subsequence/submissions/1656382490/
"""

class MySolution: #Time complexity O(n^2), Space complexity O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [1] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[j])

        return max(res)


            
