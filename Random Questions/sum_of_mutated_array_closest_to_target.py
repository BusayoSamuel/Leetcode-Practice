"""
https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/description/
"""

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        curSum = sum(arr)
        arr.sort()
        value = float("-Inf")
        if curSum <= target:
            return arr[-1]

        for r in range(len(arr) - 1, -1 , -1):
            curSum -= arr[r]

            if curSum > target:
                continue
            else:
                spotsToFill = len(arr) - r 
                res = round((target - curSum - 0.1)/spotsToFill) # "-0.1" ensures that the absolute difference is kept at minumum
                if r == 0 or (r > 0 and res >= arr[r-1]): #To ensure that only values greater than the left of the array are considered
                    value = max(res, value)

        return value

            