"""
https://leetcode.com/problems/asteroid-collision/
"""

class Solution: #Time complexity O(n), Space complexity 0(n)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]

                if diff < 0:
                    stack.pop()
                elif diff == 0:
                    a = 0
                    stack.pop()
                else:
                    a = 0

            if a:
                stack.append(a)

        return stack
    

class MySolution: #Same complexity, alternative structure
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:

            while stack and stack[-1] > 0 and a < 0:

                if abs(stack[-1]) <= abs(a):
                    if abs(a) == abs(stack.pop()):
                        a = 0
                        break
                else:
                    a = 0

            if a:
                stack.append(a)

        return stack
        
