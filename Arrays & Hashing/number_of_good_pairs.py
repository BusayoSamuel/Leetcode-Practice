"""
https://leetcode.com/problems/number-of-good-pairs/description/
"""

class MySolution: #Time complexity O(n^2), Space complexity O(1)
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    res += 1

        return res


class My2ndSolution: #Time complexity O(n), Space complexity O(n)
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
        res = 0

        for val in hashmap.values():
            pairs = (val*(val-1))//2
            res += pairs

        return res

class CleanSolution: #Time complexity O(n), Space complexity O(n)
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        res = 0

        for n in nums:
            if n in hashmap:
                res += hashmap[n]
                hashmap[n] += 1
            else:
                hashmap[n] = 1

        return res
        
