"""
https://leetcode.com/problems/rotate-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #Time complexity O(n), Space complexity O(1)
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head

        curr = head
        tail = head
        
        count = 1

        while tail.next:
            count += 1
            tail = tail.next

        k = k % count

        if not k:
            return head
        

        for i in range(count - k - 1):
            curr = curr.next

        newhead = curr.next
        tail.next = head
        curr.next = None

        return newhead