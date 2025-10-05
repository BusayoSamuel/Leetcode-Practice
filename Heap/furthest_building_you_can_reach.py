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


class AlternativeSolution: #using a min heap #Same complexity as above
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            heapq.heappush(minHeap, diff)
            if len(minHeap) > ladders: #we use ladders first and then swap for bricks when all ladders are used
                bricks -= heapq.heappop(minHeap) #swapping for bricks
                if bricks < 0: #this means we've used all ladders and all bricks
                    return i

        return len(heights) - 1
