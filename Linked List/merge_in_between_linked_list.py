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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MyOtherSolution: #Same complexity as above
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy1 = ListNode(None, list1)
        dummy2 = ListNode(None, list2)

        start1 = dummy1
        end1 = dummy1.next

        while a or b:
            if a:
                start1 = start1.next
                a -= 1
            if b:
                end1 = end1.next
                b -=1

        end1 = end1.next

        start2 = dummy2.next
        end2 = dummy2

        while end2.next:
            end2 = end2.next


        start1.next = start2
        end2.next = end1

        return dummy1.next
        
