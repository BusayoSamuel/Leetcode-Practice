"""
https://leetcode.com/problems/course-schedule-iv/description/
"""


class Solution: #Time complexity O(V*(V+E) + m), Space complexity O(V^2 + E + m) where Where m is the number of queries, V is the number of courses, and E is the number of prerequisites.
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for prereq in adj[crs]:
                    prereqMap[crs] |= dfs(prereq)
                prereqMap[crs].add(crs)
            return prereqMap[crs]

        prereqMap = {}
        for crs in range(numCourses):
            dfs(crs)

        res = []
        for u, v in queries:
            res.append(u in prereqMap[v])
        return res

class MyInefficientSolution: #Time complexity O(m * V), Space complexity O(V + E)
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        hashmap = {i:[] for i in range(numCourses)}

        for pre, course in prerequisites:
            hashmap[course].append(pre)

        def dfs(course, target):
            if not hashmap[course]:
                return False

            for pre in hashmap[course]:
                if pre == target or dfs(pre, target):
                    return True

            return False

        res = []

        for target, course in queries:
            res.append(dfs(course, target))

        return res

        
