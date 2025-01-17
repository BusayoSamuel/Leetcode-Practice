"""
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
"""

class Solution: #O(n) time complexity, #O(1) space complexity
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        l = 0

        for r in range(k-1, len(arr)):
            if l == 0:
                ave = sum(arr[l:k])/k
            else:
                ave += arr[r]/k

            if ave >= threshold:
                count+=1

            ave -= arr[l]/k
            l += 1
        
        return count
    

class AlternativeSolution: #Cleaner Version
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curSum = sum(arr[:k-1])

        for L in range(len(arr) - k + 1):
            curSum += arr[L + k - 1]
            if curSum / k >= threshold:
                res += 1
            curSum -= arr[L]

        return res

class MySolution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        curr = 0
        l = 0
        r = -1 #protects against the edge case of k == 1
        res = 0

        for r in range(k-1): #if k == 1 this wouldn't run
            curr += arr[r]

        while r + 1 < len(arr):
            r += 1
            curr += arr[r]
                
            if curr >= threshold:
                res += 1

            curr -= arr[l]
            l += 1  
            
        return res


        
