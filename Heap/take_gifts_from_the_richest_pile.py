"""
https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/
"""

class MySolution: #Time complexity O(klogn), Space complexity O(n)
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = list(map(lambda x: -x, gifts))
        heapq.heapify(gifts)
        
        for i in range(k):
            pile = heapq.heappop(gifts)
            pile = math.floor(math.sqrt(-pile))
            heapq.heappush(gifts, -pile)

        return -sum(gifts)
