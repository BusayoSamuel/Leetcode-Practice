"""
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/
"""

class Solution: #Time complexity O(nlogn), Space complexity O(n) due to sorting
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        r = len(nums) - 1
        res = 0

        for l in range(len(nums)): 
            while nums[l] + nums[r] > target and l <= r:
                r -= 1
            
            if l <= r:
                res += 2**(r-l) #This works out all the combinations you can have for this minimum value

        return res % (10**9 + 7)
        