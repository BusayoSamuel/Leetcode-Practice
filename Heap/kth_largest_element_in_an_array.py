"""
https://leetcode.com/problems/kth-largest-element-in-an-array/description/
"""
class MySolution: #Time complexity O(n + klogn), Space complexity O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * num for num in nums]
        heapq.heapify(nums)

        for i in range(k):
            res = -1 * heapq.heappop(nums)

        return res
    

class Solution: #Time complexity O(n) averge case, O(n^2) worst case, Space complexity O(n)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(l, r):
            pivot, p = r, l #use the last element as your pivot value

            for i in range(l, r): #sort the list according to the pivot
                if nums[i] <= nums[pivot]:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[pivot] = nums[pivot], nums[p]

            #the kth largest value would be at len(nums) - k

            if len(nums) - k < p: return quickselect(l, p-1) 
            elif len(nums) - k > p: return quickselect(p+1, r)
            else: return nums[p] #by sorting in this way, you guarantee that the pivot is in the right position

        return quickselect(0, len(nums)-1)    