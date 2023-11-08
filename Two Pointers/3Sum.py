"""
https://leetcode.com/problems/3sum/description/
"""

class Solution: #Time complexity O(n^2) #Space complexity O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:  #To avoid counting duplicates
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l] : #To avoid counting duplicates
                        l += 1

        return res