"""
https://leetcode.com/problems/brick-wall/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(g) where n is the total number of bricks in the wall and g is the total number of gaps
    def leastBricks(self, wall: List[List[int]]) -> int:
        postWall = []

        for row in wall:
            cur = []
            curtotal = 0
            for brick in row:
                curtotal += brick
                cur.append(curtotal)
            postWall.append(cur)

        hashmap = {}
        for row in postWall:
            for col in row:
                hashmap[col] = 1 + hashmap.get(col, 0)
        
        res = 0
        for key, value in hashmap.items():
            if key != 0 and key != sum(wall[0]):
                res = max(res, value)

        return len(wall) - res

class CleanerSolution: #Same complexity as above
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = {0: 0}

        for r in wall:
            total = 0
            for i in range(len(r) - 1):
                total += r[i]
                countGap[total] = 1 + countGap.get(total, 0)

        return len(wall) - max(countGap.values())
