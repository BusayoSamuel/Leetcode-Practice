"""
https://leetcode.com/problems/ugly-number-ii/description/
"""

class Solution: #Time complexity O(nlogn), Space complexity O(n)
    def nthUglyNumber(self, n: int) -> int:
        minheap = [1]
        visit = set()
        factors = [2, 3, 5]

        for i in range(n):
            num = heapq.heappop(minheap)
            if i == n-1:
                return num
            
            for f in factors:
                if num * f not in visit:
                    visit.add(num*f)
                    heapq.heappush(minheap, num*f)
        
