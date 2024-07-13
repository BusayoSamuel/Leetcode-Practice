"""
https://leetcode.com/problems/k-th-symbol-in-grammar/description/
"""


class MySolution: #Time complexity O(n), Space complexity O(2**(n-1))
    def kthGrammar(self, n: int, k: int) -> int:
        cur = [0]
        nxt = []

        while n - 1:
            nxt = []
            for num in cur:
                
                if num == 0:
                    nxt.append(0)
                    nxt.append(1)

                if num == 1:
                    nxt.append(1)
                    nxt.append(0)
            cur = nxt
            n -= 1

        return cur[k-1]        

class EfficientSolution: #Time complexity O(logn), Space complexity 0(1)
    def kthGrammar(self, n: int, k: int) -> int:
        cur = 0
        l, r = 1, 2**(n-1) #2**(n-1) tells us the number of values that will be in level n

        #we treat it as a tree problem and use left and right pointers to determine which child tree to traverse to
        for _ in range(n-1): #by the time we reach level n, cur ends up in position k
            m = (r + l)//2 #each level is always gonna have an even number of values so we know m would always end up on the right edge of the left portion

            if k <= m: #we to go the left sub tree and update right
                r = m
            else: #we go to the right sub tree and update left
                l = m + 1
                cur = 0 if cur else 1 #cur only changes when we go right i.e 0 -> 01, 1 -> 10, so we only update cur when going right

        return cur
