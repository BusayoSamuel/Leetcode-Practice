"""
https://leetcode.com/problems/sort-list/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class InefficientSolution: #Bubble Sort, Time complexity O(n^2), Space complexity O(1)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        while True:
            swapped = False
            prev = dummy
            curr = dummy.next

            while curr and curr.next:
                if curr.val > curr.next.val:
                    tmp = curr.next
                    nxt = curr.next.next

                    prev.next = tmp
                    tmp.next = curr
                    curr.next = nxt

                    swapped = True
                else:
                    curr = curr.next

                prev = prev.next
                

            if swapped == False: break

        return dummy.next


class BetterSolution: #MergeSort, Time complexity O(nlogn), Space complexity O(logn)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeSort(left, right)

    def getMid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeSort(self, list1, list2):
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return dummy.next

class MySolution: #Same complexity as above
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def split(node):
            slow = node
            fast = node.next 

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            l1 = node
            l2 = slow.next
            slow.next = None

            return (l1, l2)
        
        if not head or not head.next:
            return head

        l1, l2 = split(head)
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)

        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                temp = l1.next
                cur.next = l1
                cur = cur.next
                cur.next = None
                l1 = temp
            else:
                temp = l2.next
                cur.next = l2
                cur = cur.next
                cur.next = None
                l2 = temp

        if l1:
            cur.next = l1
        
        if l2:
            cur.next = l2

        return dummy.next
            



        



            


        
