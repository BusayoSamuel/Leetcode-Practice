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
            