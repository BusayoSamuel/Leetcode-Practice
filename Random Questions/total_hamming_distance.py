"""
https://leetcode.com/problems/total-hamming-distance/description/
"""

class MyInefficientSolution: #Time complexity O(n^2), Space complexity O(n^2logn) = O(n^2) due to the bin function, inefficient
    def totalHammingDistance(self, nums: List[int]) -> int:
        def hammingDistance(num1, num2):
            num1 = bin(num1).replace("0b", "")
            num2 = bin(num2).replace("0b", "")

            diff = abs(len(num1) - len(num2))

            if len(num1) < len(num2):
                num1 = ("0" * diff) + num1
            else:
                num2 = ("0" * diff) + num2

            dist = 0
            for i in range(len(num1)): # len of num1 would be approximately logn because integers are stored in 64 bit values
                if num1[i] != num2[i]:
                    dist += 1

            return dist

        total = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                total += hammingDistance(nums[i], nums[j])

        return total
                

class ApparentlyTheBestSolution: #Uses bit manipulation, Time complexity 0(n), Space complexity O(1)  
    def totalHammingDistance(self, nums: List[int]) -> int:
        
        distance = 0                  #hamming distance
        for i in range(30):
            
            mask = 1 << i             #mask will be power ith power of 2
            one , zero = 0 , 0
            for num in nums:
                
                if (num & mask):      #a bit manupulation technique to check whether the ith bit is set 
                    one +=1
                else:
                    zero +=1
            distance += (one * zero)      
            
            
        return distance
                
                