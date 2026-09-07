"""
https://leetcode.com/problems/sliding-window-maximum/description/
"""


class Solution: #Time complexity O(n), Space complexity O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        l = 0

        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r - l + 1) == k:
                res.append(nums[q[0]])
                l += 1

        return res

            
