"""
https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/
"""

class Solution: #Time complexity O(nlog(max(nums)), Space complexity O(n) due to sorting
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def isValid(threshold):
            i, cnt = 0, 0

            while i < len(nums) - 1:
                if abs(nums[i] - nums[i+1]) <= threshold: #we count all pairs that are below the max difference
                    i += 2
                    cnt += 1
                    if cnt == p: #this means there are at least p pairs with differences <= the threshold, and so this max difference is valid
                        return True
                else:
                    i += 1
            return False

        if p == 0: return 0

        l, r = 0, max(nums) #We binary search through possible max differences
        res = max(nums)

        while l <= r:
            m = (l + r)//2

            if isValid(m):
                res = m #we aim to find a lower threshold, minimising the max difference
                r = m - 1
            else:
                l = m + 1
        
        return res

