"""
https://leetcode.com/problems/sort-array-by-parity-ii/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [None for i in range(len(nums))]
        odd = 1
        even = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                res[even] = nums[i]
                even += 2
            else:
                res[odd] = nums[i]
                odd += 2

        return res

class InPlaceSolution: #Time complexity O(n), Space complexity O(n)
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = deque()
        even = deque()
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even.popleft()
            else:
                nums[i] = odd.popleft()

        return nums


class BestInPlaceSolution: #Time complexity O(n), Space complexity O(1)
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ii, i = 0, 1
        while ii < len(nums) and i < len(nums): 
            if not nums[ii] & 1: ii += 2
            elif nums[i] & 1: i += 2
            else: 
                nums[ii], nums[i] = nums[i], nums[ii]
                ii += 2
                i += 2
        return nums