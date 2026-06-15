"""
https://leetcode.com/problems/largest-rectangle-in-histogram/description/
"""


class Solution: #Time complexity O(n), Space complexity O(n)
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for index, height in enumerate(heights):
            i = index
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                res = max(res, h * (index - i))
            
            stack.append((i, height))

        index = len(heights)
        
        while stack:
            i, h = stack.pop()
            res = max(res, h * (index - i))

        return res


        
