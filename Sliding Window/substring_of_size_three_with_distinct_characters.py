"""
https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/
"""

class Solution: #Time complexity O(n), Space complexity O(1) because set is never larger than three
    def countGoodSubstrings(self, s: str) -> int:
            hashset = set(s[:3])
            l = 0
            count = 0

            if len(s) < 3:
                return 0

            for r in range(3, len(s)):
                if len(set(s[l:r])) == 3:
                    count += 1

                l += 1
        
            if len(set(s[l:])) == 3:
                    count += 1
            
            return count
    
class Solution2: #A clever way to achieve the same complexity without a set()
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        a = s[0]
        b = s[1]
        c = s[2]
        count = int(a != b and b !=c and c != a)

        for i in range(3, len(s)):
            a = b
            b = c
            c = s[i]
            count += int(a != b and b !=c and c != a)

        return count