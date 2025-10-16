"""
https://leetcode.com/problems/merge-nodes-in-between-zeros/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MySolution: #Time complexity O(n), Space complexity O(1)
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        res = head


        while cur.next and cur.next.next:
            if cur.val == 0:
                while cur.next.val != 0:
                    cur.val += cur.next.val
                    cur.next = cur.next.next

            if cur.next.next:
                cur = cur.next
            else:
                cur.next = None


        return res
        
