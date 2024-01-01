"""
https://leetcode.com/problems/boats-to-save-people/
"""

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boats = 0
        l, r = 0, len(people) - 1

        while l <= r:
            rem = limit - people[r]
            boats += 1 #becuase people[r] is always less than limit so we know a boat would at least one item
            r -= 1
            if l <= r and rem >= people[l]: # "l<=r" ensures that an index isn't counted twice, "r-=1" would move the right pointer past the left pointer in this case
                l += 1
        
        return boats