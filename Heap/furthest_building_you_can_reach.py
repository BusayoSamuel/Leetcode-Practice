"""
https://leetcode.com/problems/furthest-building-you-can-reach/description/
"""

class Solution: #Time complexity O(nlogn), Space complexity O(n)
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxheap = [] to keep track of the highest difference encountered so far

        for i in range(len(heights)-1):
            diff = heights[i+1] - heights[i]

            if diff <= 0:
                continue

            bricks -= diff #we start by attempting to use bricks
            heapq.heappush(maxheap, -diff)

            if bricks < 0: #this means we would need to swap for a ladder

                if not ladders: #hence we can't go any further
                    return i 

                ladders -= 1
                bricks += -heapq.heappop(maxheap) #we swap for the highest difference encountered so far

        return len(heights) - 1 #this means we can reach the very end
