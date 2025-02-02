"""
https://leetcode.com/problems/permutation-in-string/description/
"""

class Solution1:  #O(n) time complexity, #O(n) space complexity where n is len(s2)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {} #value:count
        l = 0

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)): #Initial comparison
            hashmap[s2[i]] = hashmap.get(s2[i], 0) + 1
            hashmap[s1[i]] = hashmap.get(s1[i], 0) - 1

        if min(hashmap.values()) == max(hashmap.values()) == 0:  #Ensures that all characters in s1 are accounted for
            return True

        for r in range(len(s1), len(s2)): #Sliding Window
            hashmap[s2[r]] = hashmap.get(s2[r], 0) + 1
            hashmap[s2[l]] -= 1
            l += 1

            if min(hashmap.values()) == max(hashmap.values()) == 0:
                return True

        return False
    

class Solution2: #Alternative structure
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {} #value:count
        l = 0

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            hashmap[s2[i]] = hashmap.get(s2[i], 0) + 1
            hashmap[s1[i]] = hashmap.get(s1[i], 0) - 1

        for r in range(len(s1), len(s2)):
            if min(hashmap.values()) == max(hashmap.values()) == 0: # Make a check first
                return True

            hashmap[s2[r]] = hashmap.get(s2[r], 0) + 1
            hashmap[s2[l]] -= 1
            l += 1    

        return min(hashmap.values()) == max(hashmap.values()) == 0


class MySolution: #Same complexity as above
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count = Counter(s1)

        l = 0

        for r in range(len(s2)):
            while r - l + 1 > len(s1):
                if s2[l] in s1count:
                    s1count[s2[l]] += 1
                l += 1

            if s2[r] in s1count:
                s1count[s2[r]] -= 1

            if min(s1count.values()) == 0 and max(s1count.values()) == 0:
                return True

        return False
        
