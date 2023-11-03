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