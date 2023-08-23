"""
https://leetcode.com/problems/validate-stack-sequences/description/
"""

class Solution: #O(n) time complexity, #O(n) space complexity
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0

        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and j < len(popped) and stack[-1] == popped[j]: #the first two conditions have to be true before the third condition can work
                stack.pop()
                j += 1 

        return not stack