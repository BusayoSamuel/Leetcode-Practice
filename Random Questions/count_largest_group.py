"""
https://leetcode.com/problems/count-largest-group/
"""

class Solution: #Time complexity O(nm) where n is the n and m is the length of n, Space complexity O(n)
    def countLargestGroup(self, n: int) -> int:
        hashmap = {} #sum of digits: count
        res = 0

        for i in range(1, n+1):
            total = 0
            for c in str(i):
                total += int(c)
            hashmap[total] = hashmap.get(total, 0) + 1

        maxCount = max(hashmap.values())

        for count in hashmap.values():
            if count == maxCount:
                res += 1

        return res
        