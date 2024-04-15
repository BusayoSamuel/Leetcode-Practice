"""
https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/description/
"""


class Solution: #Time compleixty O(nlogn) #Space complexity O(n) due to sorting
    def maximumGroups(self, grades: List[int]) -> int:
        l = 0
        r = 0
        prevSum = 0
        curSum = 0
        prevN = 0
        count = 0
        grades.sort() #sort the list to guarantee that group selection starts from the smallest numbers

        while r < len(grades):   
            curSum += grades[r]

            if curSum > prevSum and (r-l+1) > prevN: #ensure the criteria is satisfied before moving on to creating the next group
                prevSum = curSum
                prevN = r-l+1
                count += 1
                curSum = 0
                l = r + 1

            r += 1

        return count
    
class Solution: #Same complexity due to sorting
    def maximumGroups(self, grades: List[int]) -> int:
        total = 0
        curSize = 0
        grades.sort()

        while total <= len(grades):   
            curSize += 1 #if the grades are sorted we can go in groups of size 1, 2, 3... and be certain that the criteria is met for each group
            total += curSize

        return curSize - 1 #get rid of the last group that wasn't added
