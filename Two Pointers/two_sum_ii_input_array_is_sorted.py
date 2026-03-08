"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l <= r:
            total = numbers[l] + numbers[r]

            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l + 1, r + 1]


class Solution: #Time complexity O(n^2), Space complexity O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] > target:
                    break
                elif numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        

        
