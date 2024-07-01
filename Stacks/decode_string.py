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


class MySolution: #Time complexity O(n), Space complexity O(n)
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                cur = ""
                while stack[-1] != "[":
                    cur = stack.pop() + cur
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(cur * int(k))
            else:
                stack.append(c)

        return "".join(stack)
