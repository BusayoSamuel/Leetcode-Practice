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