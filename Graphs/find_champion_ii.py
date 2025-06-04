"""
https://leetcode.com/problems/find-champion-ii/submissions/1653447542/
"""

class MySolution: #Time complexity O(n), Space complexity O(n)
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        hashmap ={i:None for i in range(n)}
        res = []

        for a, b in edges:
            hashmap[b] = a

        for b, a in hashmap.items():
            if a == None:
                res.append(b)

        return -1 if len(res) > 1 else res[0]
        
