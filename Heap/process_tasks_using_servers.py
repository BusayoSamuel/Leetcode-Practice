"""
https://leetcode.com/problems/process-tasks-using-servers/
"""

class MySolution:#Time complexity O(mlogn), Space complexity O(m) where m is the number of tasks and n is the number of servers
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        freeServers = [[v, i] for i, v in enumerate(servers)]
        heapq.heapify(freeServers)
        busyServers = []
        ans = []
        i = 0
        t = 0

        while i < len(tasks):

            while busyServers:
                if busyServers[0][0] <= t:
                    timeNeeded, weight, index = heapq.heappop(busyServers)
                    heapq.heappush(freeServers, [weight, index])
                else:
                    break

            while t >= i and i < len(tasks) and freeServers:
                weight, index = heapq.heappop(freeServers)
                timeNeeded = tasks[i] + t
                heapq.heappush(busyServers, [timeNeeded, weight, index])
                ans.append(index)
                i += 1

            if not freeServers:
                t = busyServers[0][0] #if there are no free servers then we advance to the time of the next busyserver that would be free
            else:
                t += 1

        return ans

class OtherSolution: #Same complexity
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = [0] * len(tasks)

        available = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(available)
        unavail = []

        t = 0

        for i in range(len(tasks)): #we aim to assign a task on each loop
            t = max(t,i) 

            if len(available) == 0: #we ensure there are available servers for this task, if there isn't we advance time to when the next bust server would be free
                t = unavail[0][0]
            while unavail and t >= unavail[0][0]: #we free up all the busy servers that have completed their tasks
                timefree, weight, index = heapq.heappop(unavail)
                heapq.heappush(available, (weight, index))

            weight, index = heapq.heappop(available) #we pick the free server that has lowest weight and/or lowest index
            res[i] = index
            heapq.heappush(unavail, (t + tasks[i], weight, index))

        return res

            
