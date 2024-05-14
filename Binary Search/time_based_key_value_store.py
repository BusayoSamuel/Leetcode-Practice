"""
https://leetcode.com/problems/time-based-key-value-store/description/
"""

class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None: #Time complexity O(n)
        self.hashmap[key] = self.hashmap.get(key, []) + [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str: #Time complexity O(logn)
        if key not in self.hashmap:
            return ""

        l = 0
        r = len(self.hashmap[key]) - 1
        res = -1

        while l <= r:
            m = (r + l)//2

            if self.hashmap[key][m][1] > timestamp:
                r = m - 1
            elif self.hashmap[key][m][1] < timestamp:
                l = m + 1
                res = max(res, m)
            else:
                return self.hashmap[key][m][0]

        return "" if res == -1 else self.hashmap[key][res][0]


#Alternative solution
class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyStore = {}  # key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None: #Time complexity O(1)
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str: #Time complexity O(logn)
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
    
#My other solution
class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key] = self.hashmap.get(key, []) + [[timestamp, value]]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        else:
            l = 0
            r = len(self.hashmap[key]) - 1
            res = [-1, ""]

            while l <= r:
                m = (r + l)//2

                if self.hashmap[key][m][0] > timestamp:
                    r = m - 1
                elif self.hashmap[key][m][0] < timestamp:
                    res = self.hashmap[key][m]
                    l = m + 1
                else:
                    return self.hashmap[key][m][1]

            return res[1]