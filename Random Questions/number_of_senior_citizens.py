"""
https://leetcode.com/problems/number-of-senior-citizens/description/
"""
class Solution: #Time complexity O(n), Space complexity O(1)
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            if int(details[i][11:13]) > 60:
                count += 1

        return count
