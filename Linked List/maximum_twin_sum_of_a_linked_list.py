"""
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution1: #Time complexity O(n), Space complexity O(1)
    def pairSum(self, head: Optional[ListNode]) -> int:

        def findMid(head):
            slow = head
            fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            return slow

        def reverse(head):
            prev = None
            curr = head

            while curr:
                temp = curr
                curr = curr.next
                temp.next = prev
                prev = temp

            return prev

        list1 = head
        list2 = reverse(findMid(head))

        res = 0

        while list2:
            twinsum = list1.val + list2.val
            res = max(res, twinsum)
            list1 = list1.next
            list2 = list2.next

        return res
    
class Solution2: #Alternative structure
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast and fast.next: #get to the mid node and reverse the first half at the same time
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return res
