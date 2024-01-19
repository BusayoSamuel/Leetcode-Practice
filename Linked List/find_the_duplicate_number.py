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
        