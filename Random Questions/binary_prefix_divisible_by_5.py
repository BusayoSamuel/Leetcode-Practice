"""
https://leetcode.com/problems/binary-prefix-divisible-by-5/description/
"""

class InefficientSolution: #Time complexity O(n^2), Space complexity O(n)
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        def binToDec(b):
            b = b[::-1]
            dec = 0

            for i in range(len(b)):
                dec += (2 ** i) * b[i]

            return dec


        for i in range(len(nums)):
            b = nums[:i+1]
            res.append(binToDec(b) % 5 == 0) 

        return res

class Solution: #Time complexity O(n), Space complexity O(1)
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        prev = 0
        res = []

        for n in nums:
            prev = prev * 2 + n #a left shift basically doubles the values, and we add the last bit at the end
            res.append(prev % 5 == 0)

        return res