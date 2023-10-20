"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1: #Time complexity 0(n), Space complexity O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def reverse(head):
            prev = None
            curr = head

            while curr:
                tmp  = curr
                curr = curr.next
                tmp.next = prev
                prev = tmp

            return prev

        dummy = ListNode()
        dummy.next = reverse(head)
        curr = dummy

        count = 1

        while count < n:
            curr = curr.next
            count += 1

        curr.next = curr.next.next

        return reverse(dummy.next)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2: #Shorter better solution, same time complexity
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = dummy.next

        while n: #using two pointers, make sure the gap between them is appropriate
            right = right.next 
            n -= 1

        while right: #by the time right lands on a null node, left would be in the right position to delete the next node
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next