"""
https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/description/
"""

class MySolution: #Time complexity O(nlogn), Space complexity O(n)
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxheap = []

        for num in nums:
            heapq.heappush(maxheap, -int(num))

        
        for i in range(k-1):
            heapq.heappop(maxheap)

        return str(-heapq.heappop(maxheap)) 

class OtherSolution: #Same complexity
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        maxHeap = [-int(n) for n in nums]
        heapq.heapify(maxHeap)
        while k>1:
            heapq.heappop(maxHeap)
            k-=1
        return str(-maxHeap[0])


class OtherSolution: #Time complexity O(nlogk), Space complexity O(k)
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        minheap = []
        
        # Iterate through each number in the list
        for num in nums:
            # Push the integer value onto the heap
            heapq.heappush(minheap, int(num))
            # If the heap exceeds size k, pop the smallest element
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        # The root of the heap is the k-th largest element
        return str(minheap[0])
