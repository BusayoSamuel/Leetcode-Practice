"""
https://leetcode.com/problems/find-the-duplicate-number/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0 #make sure to start at 0 and not nums[0] cause nums[0] could be the duplicate
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow


class CleanerSolution: #Time complexity O(n), Space complexity O(1)
    #Because nums is between 1 and n, we can use num to represent pointers, and every num we visit is changed to its negative, that if we encounter a negative number we know we've visited it before
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            true_idx = abs(nums[i]) 
            if nums[true_idx] < 0: #we visited it before
                return true_idx
            nums[true_idx] = -nums[true_idx] #making it negative means we can still know the true_idx by using abs()

            
        
