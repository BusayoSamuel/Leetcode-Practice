"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution: #Time complexity O(n), Space complexity O(n)
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        q = deque()
        q.append(root)

        while q:
            curLen = len(q)
            for i in range(curLen):
                node = q.popleft()
                if not root:
                    continue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i + 1 < curLen:
                    print("Here")
                    node.next = q[0]

        return root


class BetterSolution: #Time complexity O(n), Space complexity O(1)
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]': 
        #Two references are used - cur and nxt, next point on nxt level are updated while on cur level
        cur = root
        nxt = cur.left if cur else None 

        while cur and nxt:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left

            cur = cur.next
            if not cur: #Means we have come to the end of a level
                cur = nxt
                nxt = cur.left

        return root
