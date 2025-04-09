"""
https://leetcode.com/problems/snakes-and-ladders/description/
"""

class Solution: 
 
    def snakesAndLadders(self, board: List[List[int]]) -> int:
      """
      Time complexity = O(n^2) as you can end up visiting all cells
      Space complexity = O(n^2) as you can end up storing moves for every square in the queue
      """
        n = len(board)
        board.reverse() #reversing the order of the rows for easier calculation

        def intToPos(square): #converting the square to its corresponding position
            r = (square - 1) // n 
            c = (square - 1) % n
            if r % 2: #checking if the row is an odd number
                c = n - 1 - c
            return r, c

        q = deque([(1, 0)]) #[square, moves]
        visit = set()

        while q: #a breadth first search is best for shortest path solutions
            square, moves = q.popleft()

            for i in range(1, 7):
                nextSquare = square + i
                r, c = intToPos(nextSquare)

                if board[r][c] != -1: #snake or ladder
                    nextSquare = board[r][c]

                if nextSquare == n * n:
                    return moves + 1

                if nextSquare not in visit: #is square is already in visit, this means a shorter path has already been found for it
                    visit.add(nextSquare)
                    q.append((nextSquare, moves + 1))


        return -1
