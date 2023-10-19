"""
https://leetcode.com/problems/online-stock-span/
"""

class StockSpanner:

    def __init__(self):
        self.stack = [] # it takes a pair of values, [price, span]
        

    def next(self, price: int) -> int: #Time complexity O(n), Space complexity O(n)
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            count += self.stack.pop()[1] # the span of recorded so no need to keep it stored in the stack 

        self.stack.append([price, count])
        return count