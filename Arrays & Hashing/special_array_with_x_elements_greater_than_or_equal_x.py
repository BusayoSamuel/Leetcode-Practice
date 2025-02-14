"""
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/
"""

class MySolution:  #Time complexity 0(nlogn), Space complexity O(n) due to sorting
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums)-1, -1, -1):
            count += 1

            if count <= nums[i]:
                if (i == 0 or (count > nums[i-1])):
                    return count
                else:
                    pass
            else:
                break
              
        return -1


class OtherSolution: #Same complexity as above
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        prev = -1
        total_right = len(nums)
        while i < len(nums):
            if nums[i] == total_right or (prev < total_right < nums[i]):
                return total_right

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            prev = nums[i]
            i += 1
            total_right = len(nums) - i

        return -1

class EfficientSolution: #Time complexity 0(n), Space complexity O(n)
    def specialArray(self, nums: List[int]) -> int:
        count = [0] * (len(nums) + 1)
        for num in nums:
            index = min(num, len(nums))
            count[index] += 1

        total_right = 0
        for i in range(len(nums), -1, -1):
            total_right += count[i]
            if i == total_right:
                return total_right
        return -1
        
