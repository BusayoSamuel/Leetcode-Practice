"""
https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/
"""

class Solution: #Time complexity O(nlogn), Space complexity O(n)
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        indexes = [i for i in range(len(times))]
        indexes.sort(key=lambda i : times[i][0])

        used_chairs = [] # (l, chair)
        available_chairs = [i for i in range(len(times))] #(chair)


        for i in indexes:
            a, l = times[i]
            while used_chairs and used_chairs[0][0] <= a:
                leave, chair = heapq.heappop(used_chairs)
                heapq.heappush(available_chairs, chair)

            chair = heapq.heappop(available_chairs)
            heapq.heappush(used_chairs, (l, chair))

            if i == targetFriend:
                return chair


        

        
