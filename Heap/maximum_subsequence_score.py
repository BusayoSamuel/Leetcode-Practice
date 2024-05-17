"""
https://leetcode.com/problems/maximum-subsequence-score/description/
"""
class MySolution: #Inefficient, Time complexity 2^n, Space complexity 2^n
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = -math.inf
        curSet = []

        def backtrack(i, total, minNums2):
            nonlocal res    

            if len(curSet) == k:
                res = max(res, total * minNums2)
                return

            if i >= len(nums1):
                return 

            curSet.append(i)
            backtrack(i+1 , total + nums1[i], min(nums2[i], minNums2))
            curSet.pop()

            backtrack(i + 1, total, minNums2)

        backtrack(0, 0, math.inf)
        return res
        

class Solution: #Time complexity O(nlogn), Space complexity O(n) due to sorting
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = list(zip(nums2, nums1))
        pairs.sort(key = lambda x: x[0], reverse = True) #we start by considering the largest possible min(nums2)
        minHeap = [] #we keep track of the lowest nums1 encountered
        heapq.heapify(minHeap)
        res = -math.inf
        n1Sum = 0

        for pair in pairs:
            n1Sum += pair[1] 
            heapq.heappush(minHeap, pair[1]) 

            if len(minHeap) == k: #we've reached a possible solution
                res = max(res, pair[0] * n1Sum)
                n1min = heapq.heappop(minHeap)
                n1Sum -= n1min  #we subtract the lowest n1 to create room for the next addition while maximising the sum of n1s encountered       

        return res

        