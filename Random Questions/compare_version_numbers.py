"""
https://leetcode.com/problems/compare-version-numbers/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        i = 0
        j = 0

        while i < len(v1) or j < len(v2):
            rev1 = int(v1[i]) if i < len(v1) else 0
            rev2 = int(v2[i]) if i < len(v2) else 0

            if rev1 > rev2:
                return 1
            elif rev1 < rev2:
                return -1
            else:
                i += 1
                j += 1
            
            
        return 0