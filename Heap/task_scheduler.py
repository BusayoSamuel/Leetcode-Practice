"""
https://leetcode.com/problems/task-scheduler/description/
"""

class Solution: #Time complexity O(n * m) where n is the number of tasks and m is n, Space complexity O(n)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, time + n))

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time