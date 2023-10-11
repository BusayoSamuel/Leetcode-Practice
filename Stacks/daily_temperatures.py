"""
https://leetcode.com/problems/daily-temperatures/description/
"""

class Solution: #Time Complexity O(n), Space complexity O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [] # pairs: [temperature, index in the list]

        for rightIndex, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]: #The number of days is found for each item that is popped 
                leftIndex = stack.pop()[1]
                answer[leftIndex] = rightIndex - leftIndex

            stack.append([temp, rightIndex])

        return answer

            
                


        