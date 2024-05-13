"""
https://leetcode.com/problems/champagne-tower/description/
"""

class MySolution: #Time complexity O(n^2), Space complexity O(n^2), where n is the total number of glasses, too much space is used
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        pyramid = []

        def dfs(size, row, col, leftover):
            if len(pyramid) < size:
                pyramid.append([0] * size)

            pyramid[row][col] = min(1, pyramid[row][col] + leftover)

            size += 1
            leftover = max(leftover-1, 0) / 2
            if leftover:
                dfs(size , row + 1, col, leftover)
                dfs(size , row + 1, col + 1, leftover)
            print(pyramid)
        
        dfs(1, 0, 0, poured)
        return pyramid[query_row][query_glass] if len(pyramid) > query_row else 0

class OptimalSolution: #Time complexity O(n^2), Space complexity O(n) where n the number of rows
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cur_row = [poured] #initialise with the total amount to be poured
        row_index = 0
        while cur_row:
            if query_row == row_index:
                return min(cur_row[query_glass], 1) #if the quantity exceeds 1, it means there'll eventually be overflow else we can be confident that the cur quantity is the final answer
            prev_row = list(cur_row) #create a reference to the previous row
            cur_row = [0] * (len(prev_row) + 1) #initialise the new row to be filled
            for i in range(len(prev_row)):
                leftover = max(prev_row[i] - 1, 0) #max capacity is 1 so if subract 1 is < 0, there's no leftover
                if leftover > 0: 
                    #we use the relationship between the position of glass in the previous row and the next row
                    cur_row[i] +=  leftover/2 
                    cur_row[i+1] += leftover/2
            row_index += 1