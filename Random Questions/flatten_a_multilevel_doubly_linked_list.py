"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class MySolution: #Time complexity O(n), Space complexity O(1)
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':


        def subflatten(node, nxt):
            cur = node
            prev = None
            while cur:
                if cur.child:
                    cur.child.prev = cur
                    cur.next = subflatten(cur.child, cur.next)
                    cur.child = None
                prev = cur
                cur = cur.next
            if nxt:
                nxt.prev = prev
            if prev:
                prev.next = nxt
            return node

        return subflatten(head, None)
        
