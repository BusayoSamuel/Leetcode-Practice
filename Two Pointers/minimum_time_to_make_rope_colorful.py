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

class MyOtherSolution: #Same complexity as above
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = 0
        res = 0
        stack = [(colors[0], neededTime[0])]

        for r in range(1, len(colors)):
            color, time = stack[-1]
            if colors[r] == color:
                if neededTime[r] >= time:
                    res += time
                    stack.pop()
                    stack.append((colors[r], neededTime[r]))
                else:
                    res += neededTime[r]
            else:
                stack.append((colors[r], neededTime[r]))

        return res

