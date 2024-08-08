"""
https://leetcode.com/problems/sum-of-subarray-minimums/description/
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n #we first assume each value is the minimum to all values on the left
        right = [n] * n #we first assume each value is the minimum to all values on the right
        stack = []


        for curIndex, curValue in enumerate(arr): #we find the furthest index to the left where the each value is the smallest
            while stack and arr[stack[-1]] >= curValue:
                stack.pop()

            if stack:
                left[curIndex] = stack[-1]

            stack.append(curIndex)

        stack = []


        for i in range(n - 1, -1, -1): #we find the furthest index to the right where the each value is the smallest,
            while stack and arr[stack[-1]] > arr[i]: #we don't include indexes with equal values to avoid duplicate counting
                stack.pop()

            if stack:
                right[i] = stack[-1]

            stack.append(i)

        res = 0

        for i in range(len(arr)):
            subarrays = (i - left[i]) * (right[i] - i) * arr[i] #(i - left[i]) * (right[i] - i) tells us the total number of subarrays where arr[i] is the minimum
            res += subarrays

        return res % (10**9 + 7)
