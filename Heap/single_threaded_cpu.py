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


class MySolution: #Same complexity as above
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        minheap = []

        for i, task in enumerate(tasks):
            tasks[i].append(i)

        tasks.sort(key=lambda x: [x[0], x[1]], reverse=True)
        curTime = tasks[-1][0]
        curTask = tasks[-1]
        res = [tasks[-1][2]]
        tasks.pop()

        while tasks or minheap:
            curTime += curTask[1]

            while tasks and tasks[-1][0] <= curTime:
                order, time, index = tasks.pop()
                print([order, time, index ])
                heapq.heappush(minheap, [time, index, order])
            
            if minheap:
                time, index, order = heapq.heappop(minheap)
                curTask = [order, time, index]
            else:
                curTask = tasks[-1]
                curTime = tasks[-1][0]
                tasks.pop()

            res.append(curTask[2])

        return res



