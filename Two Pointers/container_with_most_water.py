"""
https://leetcode.com/problems/container-with-most-water/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1)
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxA = 0

        while l < r:
            area = min(height[l], height[r]) * (r-l)
            maxA = max(maxA, area)

	
            if height[l] < height[r]:  #You priotise the larger height when considering which pointer to move next
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
                r -= 1

        return maxA

        