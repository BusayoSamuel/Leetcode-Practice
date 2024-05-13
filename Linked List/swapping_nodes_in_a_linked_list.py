"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #Time complexity O(n), Space complexity O(1)
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = head
        right = head
        end = head

        for i in range(k):
            end = end.next
            if i < k-1:
                left = left.next

        while end:
            end = end.next
            right = right.next

        left.val, right.val = right.val, left.val

        return head
    

class Solution: #Perhaps a cleaner version, same complexity
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head

        for i in range(k-1):
            curr = curr.next

        left = curr
        right = head

        while curr.next: #we know the distance from the first to last would be the same to the distance from right to last
            curr = curr.next
            right = right.next

        left.val, right.val = right.val, left.val

        return head