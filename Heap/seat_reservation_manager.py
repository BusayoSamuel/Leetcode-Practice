"""
https://leetcode.com/problems/seat-reservation-manager/description/
"""

class SeatManager: #Space complexity O(n)

    def __init__(self, n: int): #Time complexity O(n)
        self.minheap = [i for i in range(1, n + 1)]
        heapq.heapify(self.minheap) #Not necessary because the array above is already sorted
        

    def reserve(self) -> int: #Time complexity O(logn)
        idx = heapq.heappop(self.minheap)
        return idx
        

    def unreserve(self, seatNumber: int) -> None: #Time complexity O(logn)
        heapq.heappush(self.minheap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
