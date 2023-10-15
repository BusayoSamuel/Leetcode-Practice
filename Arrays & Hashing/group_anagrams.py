"""
https://leetcode.com/problems/group-anagrams/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}  
        
        for i in strs:
            group["".join(sorted(i))] = group.get("".join(sorted(i)), []) + [i]

        return group.values()