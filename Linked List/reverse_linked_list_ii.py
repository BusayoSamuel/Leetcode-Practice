"""
https://leetcode.com/problems/reverse-linked-list-ii/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NotTheCleanestSolution: #Time complexity O(n), Space complexity O(1)
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        res = head
        

        node = dummy
        count = 0

        while count != left - 1:
            node = node.next
            count += 1

        curr = node.next
        start = node

        while count != right - 1:
            node = node.next
            count += 1

        end = node.next.next

        prev = None
        tail = curr
        count = left

        while count != right + 1:
            tmp = curr
            curr = curr.next
            tmp.next = prev
            prev = tmp
            count += 1

        start.next = prev
        tail.next = end

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #Cleaner solution, same complexity
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftPrev = dummy
        cur = dummy.next

        for i in range(left-1):
            leftPrev = leftPrev.next
            cur = cur.next

        prev = None
        tail = cur

        for i in range(right - left + 1):
            tmpNext = cur.next
            cur.next = prev
            prev = cur
            cur = tmpNext

        leftPrev.next = prev
        tail.next = cur

        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MyOtherSolution: #Same complexity
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = right - left + 1
        dummy = ListNode(0, head)
        leftN = dummy
        rightN = dummy

        while count:
            rightN = rightN.next
            count -= 1

        while left - 1:
            rightN = rightN.next
            leftN = leftN.next
            left -= 1

        front = leftN
        back = rightN.next
        leftN = leftN.next

        front.next = rightN
        nxt = back
        cur = leftN

        while cur != back:
            prev = cur.next
            cur.next = nxt
            nxt = cur
            cur = prev

        return dummy.next
