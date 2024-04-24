"""
https://leetcode.com/problems/generate-parentheses/description/
"""

class MySolution: #Time complexity O(2^n), Space complexity O(n)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        lim = n * 2

        def backtrack(n, m):
            
            if len(cur) > lim or n < 0 or m < 0:
                return

            if len(cur) == lim and n == 0 and m == 0:
                if cur[-1] == ")" and cur[0] == "(":
                    res.append("".join(cur.copy()))
                return

            cur.append("(")
            backtrack(n-1, m)
            cur.pop()

            if n < m:
                cur.append(")")
                backtrack(n, m-1)
                cur.pop()

        backtrack(n, n)

        return res


class CleanerSolution: #Same complexity 
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def backtrack(open, closed):

            if open == n and closed == n:
                if cur[-1] == ")" and cur[0] == "(":
                    res.append("".join(cur)) #not need for copy here cause join create a copy already
                return

            if open < n: #an open is only added if open is < n
                cur.append("(")
                backtrack(open+1, closed)
                cur.pop()

            if open > closed: #closed is only added if open > closed i.e  "())" can never work
                cur.append(")")
                backtrack(open, closed+1)
                cur.pop()

        backtrack(0, 0)

        return res



        
        

        
        