"""
https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/
"""


class MySolution: #Time complexity O(nlogn), Space complexity O(n) due to sorting
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])


class BetterSolution: #Time complexity O(n), Space complexity O(1)
    def maxProductDifference(self, nums: List[int]) -> int:
        max1, max2, min1, min2 = 0, 0, math.inf, math.inf

        for num in nums:
            if num > max2:
                if num > max1:
                    max1, max2 = num, max1
                else:
                    max2 = num

            if num < min2:
                if num < min1:
                    min1, min2 = num, min1
                else:
                    min2 = num

        return (max1 * max2) - (min1 * min2)
