"""
https://leetcode.com/problems/k-closest-points-to-origin/description/
"""
class MySolution: #Time complexity O(nlogn), Space complexity O(n) due to sorting
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point):
            return math.sqrt(((-point[0])**2)+((-point[1])**2))

        points.sort(key=lambda x: dist(x))


        return points[:k]
    

class OptimalSolution: #Time complexity O(klogn) as we only call heappop k times, Space complexity O(n)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def dist(point):
            return ((-point[0])**2)+((-point[1])**2) #no need to find square root, if sqrt(x) > sqrt(y), then x > y

        minHeap = list(map(lambda x: [dist(x), x], points)) #need to always convert a map to list

        heapq.heapify(minHeap) 

        res = []

        while k:
            dist, point = heapq.heappop(minHeap)
            res.append(point)
            k -= 1

        return res


class MyShorterSolution: #Same complexity as above
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = [[x**2 + y**2, [x,y]] for x, y in points]

        heapq.heapify(minheap)

        res = []

        for _ in range(k):
            dist, point = heapq.heappop(minheap)
            res.append(point)

        return res


class MyOtherSolution: #Same complexity as above
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i, v in enumerate(points):
            x, y = v
            points[i] = [(x**2 + y**2), x, y]

        heapq.heapify(points)

        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(points)
            res.append([x, y])

        return res

        
