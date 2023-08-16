class Solution: #O(n) time complexity, #O(n) space complexity
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                res.append(res.pop(-2) + res.pop())
            elif tokens[i] == "-":
                res.append(res.pop(-2) - res.pop())
            elif tokens[i] == "*":
                res.append(res.pop(-2) * res.pop())
            elif tokens[i] == "/":
                res.append(int(res.pop(-2) / res.pop())) #int() function needed to truncate dividends towards zero
            else:
                res.append(int(tokens[i]))

        return res[0]