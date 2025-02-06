"""
https://leetcode.com/problems/rotate-array/description/
"""
class Solution1: #Time complexity O(n), Space complexity O(n)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = [None] * len(nums)
        for i in range(len(nums)):
            idx = (i + k) % len(nums) #This ensures the index doesn't go out of bounds and loops back
            tmp[idx] = nums[i]

        for i in range(len(nums)):
            nums[i] = tmp[i]

class Solution2: #Time complexity O(n), Space complexity O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def reverse(left, right): 
            l = left
            r = right 

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len(nums) - 1) #Reverse the entire list
        reverse(0, k - 1) #Reverse the first half
        reverse(k, len(nums) - 1) #Reverse the second half

class MuSolution: #Time complexity O(nk), Space complexity O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for _ in range(k % len(nums)):
            prev = nums[-1]
            for cur in range(len(nums)):
                temp = nums[cur]
                nums[cur] = prev
                prev = temp

