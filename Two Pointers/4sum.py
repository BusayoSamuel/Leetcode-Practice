"""
https://leetcode.com/problems/4sum/description/
"""

class Solution: #Time complexity O(n^3) #Space complexity O(n) because of sorting
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue

                l = j + 1
                r = len(nums) - 1

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total > target:
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        arr = [nums[i], nums[l], nums[r], nums[j]]
                        res.append(arr)
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
        
        return res

class Solution: #A more general solution for all kinds of sums using recursion
    def fourSum(self, nums, target):
        def findNsum(l, r, target, N, result, results):
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  
                return
            if N == 2: 
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r+1):
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

        nums.sort()
        results = []
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results
    

class MySolution: #Similar to the one above
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def sum(initialsum, initialList, count, startidx):
            if count > 2:
                for i in range(startidx, len(nums) - count + 1):
                    if  (i > startidx and nums[i] == nums[i-1]):
                        continue
                    sum(nums[i] + initialsum, initialList + [nums[i]], count - 1, i + 1)
                return #Thiline is important as it ensures that that the code below doesn't run

            l = startidx
            r = len(nums) - 1

            while l < r:
                total = initialsum + nums[l] + nums[r]

                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    res.append(initialList + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                

        sum(0, [], 4, 0)
        return res
            
