"""
https://leetcode.com/problems/decode-string/description/
"""

class Solution: #Time complexity O(n) #Space complexity O(n)
    def decodeString(self, s: str) -> str:
        stack = []
        curS = ""
        count = ""

        for i in range(len(s)):
            if s[i] == "]":
                curS = ""
                while stack[-1] != "[":
                    curS = stack.pop() + curS
                stack.pop()

                count = ""
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count
                stack.append(int(count) * curS)

            else:
                stack.append(s[i])

        return "".join(stack)