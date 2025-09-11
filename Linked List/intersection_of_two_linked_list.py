"""
https://leetcode.com/problems/intersection-of-two-linked-lists/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1: #O(n+m)  time complexity, O(n+m) space complexity
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashset = set()
        currA = headA
        currB = headB

        while currA:
            hashset.add(currA)

            currA = currA.next

        while currB:
            if currB in hashset:
                return currB

            currB = currB.next

        return None
    

class Solution2: #Elegant solution, O(n+m) time complexity, #O(1) space complexity
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB

        while l1 != l2: #If both list intersect, their last nodes will line up
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1 #l1 and l2 will either intersect at a node or None, either way the intersection gets returned


class Solution: #O(n+m)  time complexity, O(1) space complexity
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLength(head):
            length, cur = 0, head
            while cur:
                length += 1
                cur = cur.next
            return length

        m = getLength(headA)
        n = getLength(headB)
        l1, l2 = headA, headB

        if m < n:
            m, n = n, m
            l1, l2 = headB, headA

        while m - n:
            m -= 1
            l1 = l1.next

        while l1 != l2:
            l1 = l1.next
            l2 = l2.next

        return l1
