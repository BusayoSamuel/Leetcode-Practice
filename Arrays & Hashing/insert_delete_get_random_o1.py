"""
https://leetcode.com/problems/insert-delete-getrandom-o1/description/
"""

class RandomizedSet: #Time complexity O(1), Space complexity O(n)

    def __init__(self):
        self.numMap = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        self.numMap[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        idx = self.numMap[val]
        last = self.nums[-1]
        self.nums[idx] = last
        self.numMap[last] = idx
        self.nums.pop()
        del self.numMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
