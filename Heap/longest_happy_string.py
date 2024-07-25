"""
https://leetcode.com/problems/longest-happy-string/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n) if counting the length of the output else O(1)
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap = []
        for count, value in [(a, "a"),(b, "b"),(c, "c")]:
            if count:
                heapq.heappush(maxheap, (-count, value))
        res = ""

        while maxheap:
            count, value = heapq.heappop(maxheap)
            if len(res) > 1 and res[-1] == res[-2] == value: #check to ensure that you're not about to create a substring with 3 occurences of the same letter
                if not maxheap:
                    break
                count2, value2 = heapq.heappop(maxheap)
                res += value2
                count2 += 1
                if count2:
                    heapq.heappush(maxheap, (count2, value2))
            else:
                res += value
                count += 1
            if count:
                heapq.heappush(maxheap, (count, value))
        return res

            
        
