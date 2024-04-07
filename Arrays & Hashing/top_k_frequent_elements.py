"""
https://leetcode.com/problems/top-k-frequent-elements/description/
"""

class MySolution: #Time complexity O(klogn), Space complexity O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) - 1

        arr = list(zip(counter.values(), counter.keys()))

        heapq.heapify(arr)

        res = []

        while k:
            freq, value = heapq.heappop(arr)
            res.append(value)
            k -= 1

        return res
    

class OptimalSolution: #Time complexity O(n), Space complexity O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for i in range(len(nums) + 1)] #we use the index position as a reference for the freqency count - [] = values that have a freq of the index position

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for key, value in counter.items():
            freq[value].append(key)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            while freq[i] and k:
                value = freq[i].pop()
                res.append(value)
                k -= 1

            if k == 0:
                break

        return res

            

         
        

            


         
        

            