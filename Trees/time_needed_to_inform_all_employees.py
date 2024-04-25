"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/description/
"""


class MySolution: #Time complexity O(n), Space complexity O(n) using depth first search
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        hashmap = {i:[] for i in range(n)}

        for i in range(len(manager)):
            if i != headID:
                hashmap[manager[i]].append(i)


        def dfs(node):

            if not informTime[node]:
                return 0

            maxtime = 0

            for child in hashmap[node]:
                maxtime = max(maxtime, dfs(child))

            return informTime[node] + maxtime

        return dfs(headID)
    

class AlternativeSolution: #Same complexity but using breadth first search
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        hashmap = {i:[] for i in range(n)}

        for i in range(len(manager)):
            if i != headID:
                hashmap[manager[i]].append(i)


        q = deque()

        if n != 1:
            q.append((headID, 0))
        else:
            return informTime[-1]

        res = 0

        while q:
            maxtime = 0
            for i in range(len(q)):
                employee, time = q.popleft()

                res = max(res, time)  #res is continually updated on each level

                for surb in hashmap[employee]:
                    q.append((surb, time + informTime[employee])) #we add the informtime of the parent node as we progress down

        return res
    

