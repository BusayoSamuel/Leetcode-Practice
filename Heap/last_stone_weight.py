"""
https://leetcode.com/problems/last-stone-weight/description/
"""

class MySolution: #Time complexity O(nlogn) because a pop() and a push() takes logn time for each element, Space complexity O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: x * -1, stones))
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first < second:
                heapq.heappush(stones, first - second)
            
        return -stones[0] if stones else 0


class Solution: #Alternative, same complexity
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])


class MyOtherSolution: #Same complexity as above
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)

        while len(stones) > 1:
            weight1 = heapq.heappop(stones)
            weight2 = heapq.heappop(stones)

            if weight1 != weight2:
                weight = -abs(weight1-weight2)
                heapq.heappush(stones, weight)

        return -stones[0] if stones else 0
