"""
https://leetcode.com/problems/copy-list-with-random-pointer/description/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution: #Time complexity O(n), Space Complexity O(n)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {None:None}

        curr = head

        while curr:
            hashMap[curr] = Node(x=curr.val)
            curr = curr.next

        curr = head

        while curr:
            hashMap[curr].next = hashMap[curr.next] 
            hashMap[curr].random = hashMap[curr.random]
            curr = curr.next

        return hashMap[head]


class MySolution: #Same complexity as above
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        dummy = Node(0, head)
        cur = dummy.next

        while cur:
            hashmap[cur] = Node(cur.val)
            cur = cur.next

        hashmap[cur] = None

        cur = dummy.next

        while cur:
            hashmap[cur].next = hashmap[cur.next]
            hashmap[cur].random = hashmap[cur.random]
            cur = cur.next

        return hashmap[dummy.next]
        
