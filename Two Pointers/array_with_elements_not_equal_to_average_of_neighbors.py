"""
https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/description/
"""


class Solution1: #Using bubble sort considers every possible arrangement so, Time copmplexity O(n!) and Space Complexity O(1)
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        swapped = True

        while swapped:
            swapped = False
            for i in range(1, len(nums) - 1):
                ave = (nums[i-1] + nums[i + 1])/2
                if ave == nums[i]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swapped = True
        
        return nums


class Solution2: #Time complexity O(nlogn), Space complexity O(n) due to sorting
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []

        l, r = 0, len(nums)-1

        while len(res) != len(nums):#We reorder the sequence such that neighbours of each element are either less or greater than it
            res.append(nums[l])
            l += 1

            if l <= r: #To prevent appending duplicates
                res.append(nums[r])
                r -= 1
        
        return res