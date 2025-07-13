"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
"""


class MinHeap:
    def __init__(self):
        self.heap = [float("-inf")]

    def push(self, val):
        self.heap.append(val)

        i = len(self.heap) - 1

        while self.heap[i] < self.heap[i//2]:
            self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]

            i = i // 2

    def pop(self): 
        if len(self.heap) == 1:
            return None

        if len(self.heap) == 2:
            return self.heap.pop()
             
        res = self.heap[1]

        self.heap[1] = self.heap.pop()
        
        i = 1
        while i * 2 < len(self.heap):
            if (i * 2 + 1 < len(self.heap) and self.heap[i] > self.heap[i * 2 + 1] and self.heap[i * 2 + 1] < self.heap[i * 2]):
                self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]

                i = i * 2 + 1
            elif self.heap[i] > self.heap[i * 2]:
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]

                i *= 2
            else:
                break

        return res

    
class MyKthLargest:

    def __init__(self, k: int, nums: List[int]): #Time complexity O(nlogn) because pop() takes logn time and in worse youd have to pop n-k times, Space complexity O(n)
        self.heap = MinHeap()
        self.k = k

        for num in nums:
            self.heap.push(num)

        while len(self.heap.heap) > k + 1:
            self.heap.pop()

        

    def add(self, val: int) -> int: #Time complexity O(logn), Space complexity O(1)
        self.heap.push(val)
        if len(self.heap.heap) > self.k + 1:
            self.heap.pop()

        return self.heap.heap[1]

class CleanerKthLargest: #Using built-in functions

    def __init__(self, k: int, nums: List[int]): #Same complexity
        self.heap = nums
        self.k = k

        heapq.heapify(nums)

        while len(self.heap) > k:
            heapq.heappop(self.heap)


    def add(self, val: int) -> int: #Same complexity
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
        
