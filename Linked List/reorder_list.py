"""
https://leetcode.com/problems/reorder-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  #Time Complexity: O(n), Space Complexity: O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def getMid(node):
            slow = node
            fast = node.next #this ensures that the slow pointer stops just before the middle

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            tmp = slow
            slow = slow.next
            tmp.next = None #now we can set the tail of l1 to none before getting l2

            return slow


        def reverse(node):
            prev = None
            curr = node

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            return prev
        

        l1 = head
        l2 = reverse(getMid(head))

        while l1 and l2:
            #1st pick is from l1
            tmp = l1
            l1 = l1.next
            tmp.next = l2
            
            #2nd pick from l2
            tmp = l2
            l2 = l2.next
            tmp.next = l1

class MySolution: #Same complexity as above
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return head
            
        def reverse(node):
            prev = None
            cur = node

            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            return prev

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = head
        l2 = slow.next
        slow.next = None

        l2 = reverse(l2)

        while l2:
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2

        return head
