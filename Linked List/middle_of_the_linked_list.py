"""
https://leetcode.com/problems/middle-of-the-linked-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #O(n) time complexity, #O(1) space complexity
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


class OtherSolution: #Same complexity as above
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n, cur = 0, head
        while cur:
            cur = cur.next
            n += 1

        n //= 2
        cur = head
        while n:
            n -= 1
            cur = cur.next
        return cur
