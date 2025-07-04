"""
https://leetcode.com/problems/minimum-index-of-a-valid-split/description/
"""


class Solution: #Time complexity O(n), Space complexity O(n)
    def minimumIndex(self, nums: List[int]) -> int:
        left = defaultdict(int)
        right = Counter(nums)

        for i in range(len(nums)):
            left[nums[i]] += 1
            right[nums[i]] -= 1

            left_len = i + 1
            right_len = len(nums) - i - 1

            if 2 * left[nums[i]] > left_len and 2 * right[nums[i]] > right_len:
                return i

        return -1


class Solution: #Time complexity O(n), Space complexity O(1)
    def minimumIndex(self, nums: List[int]) -> int:
        majority = count = 0
        for num in nums:
            if count == 0:
                majority = num
            count += (1 if majority == num else -1)

        left_cnt, right_cnt = 0, nums.count(majority)

        for i in range(len(nums)):
            if nums[i] == majority:
                left_cnt += 1
                right_cnt -= 1

            left_len = i + 1
            right_len = len(nums) - i - 1

            if 2 * left_cnt > left_len and 2 * right_cnt > right_len:
                return i

        return -1


