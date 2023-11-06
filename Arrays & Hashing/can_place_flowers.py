"""
https://leetcode.com/problems/can-place-flowers/description/
"""

class Solution1: #Time complexity O(n), Space complexity O(n)
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0] #This covers the edge case of an array that starts or ends with zero

        for i in range(1, len(f) - 1):
            if not f[i-1] and not f[i] and not f[i + 1]:
                f[i] = 1
                n -= 1

        return n <= 0
    
class Solution2: #Time complexity O(n), Space complexity O(1)
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = 0 if flowerbed[0] else 1 #This covers the edge case of an array that starts with zero

        for f in flowerbed:
            if f:
                n -= int((empty - 1)/2) #3 contiguous zeros means that a flower can be place there
                empty = 0
            else:
                empty += 1

        n -= int(empty/2) #This covers the edge case of an array that ends with zero
        return n <= 0