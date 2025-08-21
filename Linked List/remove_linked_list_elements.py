"""
https://leetcode.com/problems/remove-linked-list-elements/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1: #O(n) time complexity, #O(1) space complexity
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while curr:
            while curr.next and curr.next.val == val: #needs to be a while to catch a series of duplicates
                curr.next = curr.next.next

            curr = curr.next

        return dummy.next
    

class Solution2: #Alternative solution, using two pointers 
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, curr = dummy, dummy.next

        while curr:
            if curr.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next

            curr = curr.next

        return dummy.next


