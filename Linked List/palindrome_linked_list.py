"""
https://leetcode.com/problems/palindrome-linked-list/description/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #O(n) time complexity, #O(1) space complexity
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.findMid(head)
        l1 = self.reverse(mid)
        l2 = head

        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
    
    def findMid(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev