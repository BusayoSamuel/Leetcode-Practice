"""
https://leetcode.com/problems/destination-city/description/
"""

class MySolution: #Time complexity O(n), Space complexity 0(1)
    def destCity(self, paths: List[List[str]]) -> str:
        hashmap = {}
        for path in paths:
            start = path[0]
            end = path[1]

            hashmap[start] = end
            if end not in hashmap:
                hashmap[end] = None


        for start in hashmap.keys():
            if not hashmap[start]:
                return start
            
        


class CleanerSolution: #Same complexity
    def destCity(self, paths: List[List[str]]) -> str:
        hashset = set()

        for path in paths:
            hashset.add(path[0])

        for path in paths:
            if path[1] not in hashset:
                return path[1]
