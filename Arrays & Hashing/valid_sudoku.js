/*
https://leetcode.com/problems/valid-sudoku/description/
*/


class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     * Time complexity O(1), Space complexity O(1)
     */
    isValidSudoku(board) {
        const cols = Array.from({length: board[0].length}, () => new Set());
        const rows = Array.from({length: board.length}, () => new Set());
        const grid = Array.from({length: 3}, () => Array.from({length: 3}, () => new Set()));

        for (let r = 0; r < board.length; r ++){
            for (let c = 0; c < board[0].length; c++){
                if (board[r][c] === ".") continue;
                if (cols[c].has(board[r][c])
                    || rows[r].has(board[r][c])
                    || grid[Math.floor(r/3)][Math.floor(c/3)].has(board[r][c])        
                ){
                    return false
                }
                else{
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    grid[Math.floor(r/3)][Math.floor(c/3)].add(board[r][c])
                }
            }
        }
        return true
    }
}
