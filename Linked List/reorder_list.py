"""
https://leetcode.com/problems/reorder-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #Time Complexity: O(n), Space Complexity: O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        list1 = head
        list2 = self.reverse(self.split(head))

        while list1 and list2:
            temp1 = list1
            temp2 = list2

            list1 = list1.next
            list2 = list2.next

            temp1.next = temp2
            temp2.next = list1

    def split(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        return mid

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

        

