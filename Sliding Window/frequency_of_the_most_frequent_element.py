"""
https://leetcode.com/problems/frequency-of-the-most-frequent-element/
"""

class Attempt: #O(n^2logn) time complexity #O(n) space complexity, Not efficient enough 
    def maxFrequency(self, nums: List[int], k: int) -> int:
        maxf = 1
        opCount = {} #Value:sorted list of ops needed

        for i in range(len(nums)):
            ops = []
            for j in range(len(nums)):
                op = nums[i] - nums[j]
                if op >= 0:
                    ops.append(op)
            opCount[nums[i]] = sorted(ops)

        for i in opCount.values():
            ops = k
            j = 0
            count = 0
            while i and j < len(i) and ops-i[j] >= 0:
                count += 1
                ops -= i[j]
                j += 1
            maxf = max(maxf, count)

        return maxf
    
class Solution: #O(nlogn) time complexity, #0(1) space complexity
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        l , r = 0, 0
        total, res = 0, 0

        while r < len(nums):
            total += nums[r]

            while nums[r] * (r-l+1) > total + k:
                total -= nums[l]
                l += 1

            res = max(res, r-l+1)
            r += 1

        return res