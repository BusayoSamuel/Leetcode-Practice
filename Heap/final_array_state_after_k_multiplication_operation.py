"""
https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/
"""

class MySolution: #Time complexity O(nlogn), Space complexity O(n)
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:  
        nums = [[nums[i], i] for i in range(len(nums))]
        heapq.heapify(nums)

        for _ in range(k):
            x, i = heapq.heappop(nums)
            heapq.heappush(nums, [x*multiplier, i])

        nums.sort(key=lambda x: x[1])
        nums = [nums[i][0] for i in range(len(nums))]
        return nums

class BetterSolution: #Time complexity O(klogn), Space complexity O(n)
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]: 
        res = nums[::] 
        nums = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(nums)

        for _ in range(k):
            x, i = heapq.heappop(nums)
            res[i] *= multiplier
            heapq.heappush(nums, (res[i], i))

        return res
        
        
