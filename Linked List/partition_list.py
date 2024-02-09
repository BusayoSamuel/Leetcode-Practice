"""
https://leetcode.com/problems/partition-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #Time complexity O(n), Space complexity O(1)
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        res = ListNode()
        nxt = res

        while cur.next:
            if cur.next.val < x:
                nxt.next = cur.next
                nxt = nxt.next
                cur.next = cur.next.next
            else:
                cur = cur.next

        nxt.next = dummy.next

        return res.next
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class AlternativeSolution: #Different structure, same complexity
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        res = ListNode()
        nxt = res

        while cur.next:
            if cur.next.val < x:
                nxt.next = cur.next
                nxt = nxt.next
                cur.next = cur.next.next
            else:
                cur = cur.next

        nxt.next = dummy.next

        return res.next