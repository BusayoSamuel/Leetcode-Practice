"""
https://leetcode.com/problems/basic-calculator-ii/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        pre_op = "+"
        s += "+"

        for c in s:
            if c in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                num = num * 10 + int(c)
            elif c == " ":
                continue
            else:
                if pre_op == "+":
                    stack.append(num)
                elif pre_op == "-":
                    stack.append(-num)
                elif pre_op == "*":
                    operant = stack.pop()
                    stack.append(operant*num)
                elif pre_op == "/":
                    operant = stack.pop()
                    stack.append(math.trunc(operant/num)) #better than "//" ensures that if you divide a negative number it is rounded upwards
                pre_op = c
                num = 0
        
        return sum(stack)
        