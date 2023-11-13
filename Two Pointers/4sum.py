"""
https://leetcode.com/problems/4sum/description/
"""

class Solution: #Time complexity O(n^3) #Space complexity O(n) because of sorting
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue

                l = j + 1
                r = len(nums) - 1

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total > target:
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        arr = [nums[i], nums[l], nums[r], nums[j]]
                        res.append(arr)
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
        
        return res
            