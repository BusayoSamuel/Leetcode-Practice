"""
https://leetcode.com/problems/matchsticks-to-square/description/
"""

class MySolution: #Time complexity O(4^n), Space complexity O(n)
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
            
        target = sum(matchsticks)//4
        left = 0
        right = 0
        top = 0
        bottom = 0
        res = False

        matchsticks.sort(reverse=True)

        def backtrack(i):
            nonlocal res
            nonlocal target
            nonlocal left
            nonlocal bottom
            nonlocal right
            nonlocal top

            if i >= len(matchsticks):
                    return True

            if left + matchsticks[i] <= target:
                left += matchsticks[i]
                if backtrack(i+1):
                    return True
                left -= matchsticks[i]

            if right + matchsticks[i] <= target:
                right += matchsticks[i]
                if backtrack(i+1):
                    return True
                right -= matchsticks[i]

            if top + matchsticks[i] <= target:
                top += matchsticks[i]
                if backtrack(i+1):
                    return True
                top -= matchsticks[i]

            if bottom + matchsticks[i] <= target:
                bottom += matchsticks[i]
                if backtrack(i+1):
                    return True
                bottom -= matchsticks[i]

            return False

        
        return backtrack(0)


class CleanerSolution: #Same complexity
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0: #check if it's even possible to 4 integer sides
            return False
            
        target = sum(matchsticks)//4
        sides = [0] * 4

        matchsticks.sort(reverse=True) #makes it quciker to determine if it's possible to make a square if the largest matchstick is bigger than the target side length

        def backtrack(i):

            if i >= len(matchsticks):
                    return True

            for j in range(4): #try placing a matchstick in every side 
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j] -= matchsticks[i]

            return False

        
        return backtrack(0)

            

            


            

            
