"""
https://leetcode.com/problems/remove-nodes-from-linked-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MySolution: #Time complexity O(n), Space complexity O(1)
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            dummmy = ListNode(0, node)
            prev = None
            cur = node

            while cur:
                temp = cur
                cur = cur.next
                temp.next = prev
                prev = temp

            return prev


        cur = reverse(head)
        tail = cur

        while cur:
            while cur.next and cur.next.val < cur.val:
                cur.next = cur.next.next

            if not cur.next:
                break

            cur = cur.next

        res = reverse(tail)

        return res

class MyOtherSolution: #Same complexity as above
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            cur = node

            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            return prev


        head = reverse(head)
        cur = head
    
        while cur:
            while cur.next and cur.next.val < cur.val:
                cur.next = cur.next.next
            cur = cur.next

        return reverse(head)
