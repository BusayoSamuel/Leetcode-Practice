"""
https://leetcode.com/problems/add-two-numbers/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #Time complexity O(n), Space complexity O(n) where n is the size of the largest list
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            ans = v1 + v2 + carry
            val = ans % 10
            carry = ans // 10

            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

class MyAlternativeSolution: #Same complexity
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        rem = 0
        
        while l1 or l2 or rem:
            total = rem

            if l1:
                total += l1.val

            if l2:
                total += l2.val

            rem = total // 10
            val = total % 10

            node = ListNode(val)

            res.next = node
            res = res.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next

