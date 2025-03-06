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


class MySolution: #Same complexity as above
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0

        r = len(nums) - 1 #really key to start r from the end to avoid the repeated work, we're considering the next minimum in each loop so need to consider higher values of max each time
        for l in range(len(nums)):

            while l <= r and nums[l] + nums[r] > target:
                r -= 1

            if r < l: #this suggest to no other minimum would work so we can close here
                break

            res += 2**(r - l) 


        return res % (10**9 + 7)


        
