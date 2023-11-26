"""
https://leetcode.com/problems/majority-element/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)
        
        for num, count  in hashmap.items():
            if count > len(nums)/2:
                return num
            

class Solution: #Time complexity O(n), Space complexity O(1)
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0 #res keeps track of which element is dominating the length of the list so far

        for i in range(len(nums)):
            if count == 0:
                res = nums[i]
            
            count += 1 if nums[i] == res else -1

        return res