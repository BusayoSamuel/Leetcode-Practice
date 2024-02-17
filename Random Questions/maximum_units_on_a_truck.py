"""
https://leetcode.com/problems/maximum-units-on-a-truck/description/
"""

class Solution: #Time complexity O(nlogn) due to sorting, Space complexity O(n) due to sorting
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True) #can also do boxTypes.sort(key = lambda x: x[1], reverse = True)
        res = 0

        for box in boxTypes:
            multi = min(box[0], truckSize) #determines how much boxes we can take without exceeding the current trucksize
            truckSize -= multi
            res += multi * box[1]
            
            if truckSize == 0:
                break

        return res