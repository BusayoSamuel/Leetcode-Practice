"""
https://leetcode.com/problems/binary-subarrays-with-sum/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def slide(x):
            if x < 0:
                return 0

            l = 0
            total = 0
            res = 0
            for r in range(len(nums)):
                total += nums[r]

                while l <= r and total > x:
                    total -= nums[l]
                    l += 1

                res += r-l+1  #we're adding all arrays that end with array nums[r] between nums[r] and nums[l] on each pass

            return res

        return slide(goal) - slide(goal-1) #Say is goal is 2, to get the subarrays we use sliding window for arrays with sum <= 2 and subtract arrays with sum <= 1 from it
