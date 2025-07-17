"""
https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/
"""

class MySolution: #Time complexity O(n), Space complexity O(n)
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        res = 0
        l = 0

        for r in range(len(nums)):
            hashmap[nums[r]] += 1

            while hashmap[nums[r]] > k:
                hashmap[nums[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


class MyOtherSolution: #Same complexity as above
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(nums)):
            count[nums[r]] += 1

            while l <= r and count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1

            res = max(res, r-l+1)


        return res


        
            
