"""
https://leetcode.com/problems/encode-and-decode-strings/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)

    def __init__(self):
        self.hashmap = {}
        self.pointer = 0

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(self.pointer)
            res += ","
            self.hashmap[self.pointer] = s
            self.pointer += 1

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        for c in s.split(",")[0:-1]:
            res.append(self.hashmap[int(c)])

        return res

