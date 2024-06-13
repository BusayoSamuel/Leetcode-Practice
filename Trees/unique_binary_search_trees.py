"""
https://leetcode.com/problems/unique-binary-search-trees/description/
"""

class Solution: #Time complexity(n^2), Space complexity O(n)
    def numTrees(self, n: int) -> int:
        numTreesFor = [1] * (n+1) #includes a tree with length size 0  

        for numNodes in range(2, n + 1): #we know for len[0] and len[1] the numTrees would be 1, so we start from 2
            total = 0
            for root_idx in range(1, numNodes + 1):# "numNodes + 1" to include numNodes as well
                numLeftNodes = root_idx - 1
                numRightNodes = numNodes - root_idx
                total += numTreesFor[numLeftNodes] * numTreesFor[numRightNodes]
            numTreesFor[numNodes] = total

        return numTreesFor[n]
        
