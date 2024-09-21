"""
https://leetcode.com/problems/find-the-town-judge/description/
"""


class Solution: #Time complexity O(n), Space complexity O(n)
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hashmap = {i: set() for i in range(1, n + 1)}

        for person in trust:
            truster = person[0]
            trustee = person[1]
            hashmap[truster].add(trustee)

        pos = None
        for truster in hashmap:
            if not hashmap[truster]:
                if not pos:
                    pos = truster
                else:
                    return -1

        if not pos:
            return -1

        for trustees in hashmap.values():
            if trustees and pos not in trustees:
                return -1

        return pos 


class CleanerSolution: #Same complexity
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = [0] * (n + 1)
        outgoing = [0] * (n + 1)

        for src, des in trust:
            incoming[des] += 1
            outgoing[src] += 1

        for i in range(1, n+1):
            if incoming[i] == n-1 and outgoing[i] == 0:
                return i

        return -1


class CleanestSolution: #Same complexity
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = [0] * (n + 1)

        for src, des in trust:
            delta[des] += 1
            delta[src] -= 1

        for i in range(1, n+1):
            if delta[i] == n-1:
                return i

        return -1

        

        
