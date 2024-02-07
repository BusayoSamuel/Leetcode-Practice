"""
https://leetcode.com/problems/online-stock-span/
"""

class StockSpanner:

    def __init__(self):
        self.stack = [] # it takes a pair of values, [price, span]
        

    def next(self, price: int) -> int: #Time complexity O(n), Space complexity O(n)
        count = 1
        while self.stack and self.stack[-1][0] <= price: #In the worst case only one of the prices would need to loop through the length of the stack so time complexity is O(n + n) => O(n)
            count += self.stack.pop()[1] # the span is recorded so no need to keep it stored in the stack 

        self.stack.append([price, count])
        return count
