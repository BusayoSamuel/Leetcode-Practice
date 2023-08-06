"""
https://leetcode.com/problems/concatenation-of-array/
"""

class Solution: #O(n) time complexity, #O(1) space complexity
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums