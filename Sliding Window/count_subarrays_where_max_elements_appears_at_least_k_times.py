"""
https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/
"""

class MySolution: #Inefficient, Time complexity O(n^2), Space complexity O(1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        maxInt = max(nums)

        for i in range(len(nums)):
            count = 0
            for j in range(i, len(nums)):
                if nums[j] == maxInt:
                    count += 1
                if count >= k:
                    res += 1
        
        return res

class MyEffiecientSolution: #Time complexity O(n), Space complexity O(1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        max_n = max(nums)
        count = 0

        for r in range(len(nums)):
            if nums[r] == max_n:
                count += 1

            while count >= k:
                if nums[l] == max_n:
                    count -= 1
                l += 1

            res += l

        return res


        
