"""
https://leetcode.com/problems/single-threaded-cpu/description/
"""

class Solution: #Time complexity O(nlogn), Space complexity O(n)
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx, arr in enumerate(tasks): #we append the index of each task as the minHeao would need it for comparisons
            arr.append(idx)

        tasks.sort()

        i = 0
        minHeap = []
        res = []
        time = tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]: #We add any tasks where time has passed their enqueue time
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]] ) #the minHeap only needs the proccessing time or the index to judge the order of tasks
                i += 1

            if minHeap: 
                procTime, idx = heapq.heappop(minHeap)
                time += procTime #This ensure that we can skip on to the next tasks in the heap
                res.append(idx)
            else:
                time = tasks[i][0] #This ensures that we end up adding a new task to the heap


        return res
