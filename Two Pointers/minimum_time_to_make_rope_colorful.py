"""
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(n)
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stack = []
        res = 0

        for i, c in enumerate(colors):
            if stack and stack[-1][0] == c:
                if stack[-1][1] < neededTime[i]:
                    res += stack.pop()[1]
                    stack.append([c, neededTime[i]])
                else:
                    res += neededTime[i]
            else:
                stack.append([c, neededTime[i]])

        return res
