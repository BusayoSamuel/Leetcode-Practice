"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""

class Solution: #Time complexity O(logn), Space complexity O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        def search(left):
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = (r+l)//2

                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    if left:
                        res[0] = m if res[0] == -1 else min(res[0], m) 
                        r = m - 1 #This move the mid pointer towards the leftmost edge
                    else:
                        res[1] = m if res[0] == -1  else max(res[1], m)
                        l = m + 1 #This move the mid pointer towards the rightmost edge
                    
        search(True)
        search(False)

        return res
    

    class MySolution: #Time complexity O(n), Space complexity O(1)
        def searchRange(self, nums: List[int], target: int) -> List[int]:
            l = 0
            r = len(nums) - 1
            res = [-1, -1]

            while l <= r:
                m = (l+r)//2

                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    res[0] = m
                    res[1] = m

                    while res[0] - 1 >= 0 and nums[res[0]] == nums[res[0]-1]:
                        res[0] -= 1

                    while res[1] + 1 < len(nums) and nums[res[1]] == nums[res[1]+1]:
                        res[1] += 1

                    break
                    
            return res
                