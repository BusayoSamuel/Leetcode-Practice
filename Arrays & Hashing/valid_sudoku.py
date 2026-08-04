"""
https://leetcode.com/problems/valid-sudoku/description/
"""

class MySolution: #Time complexity O(1), Space complexity O(1) cause the size of sudoko cells is fixed at 9 x 9 
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:set() for i in range(9)}
        cols = {i:set() for i in range(9)}
        boxes = {(i // 3, j // 3) :set() for i in range(9) for j in range(9)}

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    if ((board[i][j] in rows[i]) or 
                        (board[i][j] in cols[j]) or 
                        (board[i][j] in boxes[(i//3), (j//3)])):
                        return False
                    else:
                        rows[i].add(board[i][j])
                        cols[j].add(board[i][j])
                        boxes[(i//3), (j//3)].add(board[i][j])

        return True


class MyOtherSolution: #Same complexity as above
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for i in range(len(board[0]))]
        rows = [set() for i in range(len(board))]
        grid = [ [set() for i in range(3)] for j in range(3)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in cols[c]:
                        return False
                    else:
                        cols[c].add(board[r][c])
                    
                    if board[r][c] in rows[r]:
                        return False
                    else:
                        rows[r].add(board[r][c])

                    if board[r][c] in grid[r // 3][c // 3]:
                        return False
                    else:
                        grid[r // 3][c // 3].add(board[r][c])

        return True
        
