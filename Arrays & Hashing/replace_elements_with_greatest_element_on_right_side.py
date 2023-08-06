"""
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
"""

class Solution: #O(n) time complexity, O(1) space complexity
    def replaceElements(self, arr: List[int]) -> List[int]:
        currmax = -1

        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = currmax
            currmax = max(currmax, temp)

        return arr