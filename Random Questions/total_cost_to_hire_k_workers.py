"""
https://leetcode.com/problems/total-cost-to-hire-k-workers/description/
"""

class Solution: #Time complexity O(klogn), Space complexity O(n)
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        leftHeap = costs[:candidates]
        rightHeap = costs[max(len(costs)-candidates, candidates):] #helps to cover cases where len(costs) < candidates
        heapq.heapify(leftHeap)
        heapq.heapify(rightHeap)
        cost = 0

        i, ii = candidates, len(costs) - candidates - 1 #to keep track of what costs have been added to each heap
        for _ in range(k):
            if not rightHeap or leftHeap and leftHeap[0] <= rightHeap[0]:
                cost += heapq.heappop(leftHeap)
                if i <= ii: #prevents a double addition to heaps
                    heapq.heappush(leftHeap, costs[i])
                    i += 1
            else:
                cost += heapq.heappop(rightHeap)
                if ii >= i: # prevents a double addition to heaps
                    heapq.heappush(rightHeap, costs[ii])
                    ii -= 1
            
        return cost
