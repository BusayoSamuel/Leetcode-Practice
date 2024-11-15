"""
https://leetcode.com/problems/set-mismatch/description/
"""

class MySolution:  #Time complexity O(n), Space complexity O(n)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        found = set()
        twice = None
        missing = None

        for i in range(len(nums)):
            if nums[i] in found:
                twice = nums[i]

            found.add(nums[i])

        for i in range(1, len(nums) + 1):
            if i not in found:
                missing = i
                break

        return [twice, missing]


class EfficientSolution: #Time complexity O(n), Space complexity O(1)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [None, None]
        
        for n in nums:
            n = abs(n)
            if nums[n-1] < 0: #means we've visited this number already, this is the duplicate
                res[0] = n
            else:
                nums[n-1] = -nums[n-1] #each position visited is marked as negative

        for i, n in enumerate(nums):
            if n > 0:
                res[1] = i + 1 #the missing value would be a step ahead of the position 

        return res

        
