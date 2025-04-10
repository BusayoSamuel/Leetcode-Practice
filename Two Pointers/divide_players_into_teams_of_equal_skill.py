"""
https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/
"""

class Solution: 
  """
  Time complexity O(n) as we iterate to each value in the list
  Space complexity O(n) as we create a hashmap to count each value in the input list
  """

    def dividePlayers(self, skill: List[int]) -> int:
        skillCount = Counter(skill)
        res = 0
        target = int((sum(skill)/len(skill))*2)

        for n in skill:
            if not skillCount[n]:
                continue 

            skillCount[n] -= 1
            if (target - n) not in skillCount or not skillCount[target - n]:
                return -1

            res += n * (target - n)
            skillCount[target - n] -= 1

        return res
