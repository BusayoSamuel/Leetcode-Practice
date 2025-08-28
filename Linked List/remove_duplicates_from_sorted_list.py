"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #O(n) time complexity, #0(1) space complexity
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 

        prev, curr = head, head.next

        while curr:
            if prev.val == curr.val:
                prev.next = prev.next.next
            else:
                prev = curr
            
            curr = curr.next

        return head

class MySolution: #Same complexity as above
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashset = set()
        dummy = ListNode(None, head)
        cur = dummy

        while cur and cur.next:
            while cur.next and cur.next.val in hashset:
                cur.next = cur.next.next
            if cur.next:
                hashset.add(cur.next.val)

            cur = cur.next

        return dummy.next
        
