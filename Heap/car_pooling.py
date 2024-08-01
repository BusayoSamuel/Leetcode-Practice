"""
https://leetcode.com/problems/car-pooling/description/
"""

class Solution: #Time complexity O(nlogn), Space complexity O(n)
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda x:x[1])
        minHeap = []
        cur = 0

        for trip in trips:
            curNum, curStart, curEnd = trip
            cur += curNum

            while minHeap and minHeap[0][0] <= curStart:
                end, num = heapq.heappop(minHeap)
                cur -= num

            if cur > capacity:
                return False

            heapq.heappush(minHeap, (curEnd, curNum))

        return True


class Solution: #Time complexity O(n), Space complexiy O(1)
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changeInPass = [0] * 1001

        for trip in trips:
            num, start, end = trip
            changeInPass[start] += num
            changeInPass[end] -= num

        curPass = 0
        for change in changeInPass:
            curPass += change
            if curPass > capacity:
                return False
        return True
