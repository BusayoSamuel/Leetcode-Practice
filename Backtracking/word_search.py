"""
https://leetcode.com/problems/word-search/description/
"""


class Solution: #Time complexity O(n*m*4^o), Space complexity O(n*m*4^o) where n is the size of row, m is the size of columns and o is the size of words
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        path = set() #important to keep track of cells you've visited already

        def backtrack(i, j, k):
            if k >= len(word):
                return True

            if (i < 0 or 
                j < 0 or 
                i >= m or 
                j >= n or  
                board[i][j] != word[k] or 
                (i, j) in path):
                return False

            path.add((i, j))

            res = (backtrack(i, j + 1, k + 1) or
                    backtrack(i, j - 1, k + 1) or
                    backtrack(i + 1, j, k + 1) or
                    backtrack(i - 1, j, k + 1)) #we just need one of these paths to be true
            
            path.remove((i,j)) #need to remove path visited as we pop back to a new alternative
            return res


        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False

class MySolution: #Same complexity
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])

        hashset = set()

        def backtrack(i, j, cur):
            if (i,j) in hashset:
                return False

            hashset.add((i,j))

            if board[i][j] != word[cur]:
                hashset.remove((i,j))
                return False

            if cur == len(word) - 1:
                return True

            if i + 1 < m:
                if backtrack(i + 1, j, cur + 1):
                    return True

            if j + 1 < n:
                if backtrack(i, j + 1, cur + 1):
                    return True

            if i - 1 >= 0:
                if backtrack(i - 1, j, cur + 1):
                    return True

            if j - 1 >= 0:
                if backtrack(i, j - 1, cur + 1):
                    return True

            hashset.remove((i,j))
            return False


        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False
        
