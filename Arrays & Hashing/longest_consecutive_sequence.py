"""
https://leetcode.com/problems/longest-consecutive-sequence/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        res = 0

        hashset = set(nums)

        for num in nums:
            if num - 1 in hashset: #then we know we are at the start of a potential sequence
                continue

            while num in hashset: #we count each num that comes after the start
                hashset.remove(num) #a number can only be part of one sequence so we need not to consider them twice
                count += 1
                num += 1

            res = max(res, count)
            count = 0

        return res


class AnotherSolution: #Same complexity as above
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in hashset:
                count = 1
                cur = num + 1

                while cur in hashset:
                    count += 1
                    cur += 1

                res = max(count, res)

        return res
        
