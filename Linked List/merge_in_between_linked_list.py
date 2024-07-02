"""
https://leetcode.com/problems/merge-in-between-linked-lists/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MySolution: #Time complexity O(n), Space complexity O(1)
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l2_head = list2
        l2_tail = list2

        while l2_tail.next != None:
            l2_tail = l2_tail.next

        l1_start = list1
        count = 1
        while count != a:
            l1_start = l1_start.next
            count += 1

        l1_end = l1_start
        while count != b + 2:
            l1_end = l1_end.next
            count += 1

        l1_start.next = l2_head
        l2_tail.next = l1_end

        return list1
