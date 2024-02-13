"""
https://leetcode.com/problems/score-of-parentheses/
"""

class Solution: #Time complexity O(n), #Space complexity O(n)
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0] 

        for c in s:
            if c == "(":
                stack.append(0)
            else:
                value = max(2 * stack.pop(), 1) #If an opening bracket precedes it, then than means we simply have a value of 1,
						# else that means this bracket is within another bracket so we have to double


                stack[-1] += value #preceding complete set of brackets on the same level are added together

        return stack[-1]