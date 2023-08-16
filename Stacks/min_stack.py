"""
https://leetcode.com/problems/min-stack/description/
"""

class MinStack: #O(1) time complexity, #O(n) space complexity
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            newmin = val
        else:
            newmin = min(self.stack[-1][1], val)
        self.stack.append([val, newmin])        

    def pop(self) -> None:
        return self.stack.pop()[0]  

    def top(self) -> int:
         return self.stack[-1][0]  

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()