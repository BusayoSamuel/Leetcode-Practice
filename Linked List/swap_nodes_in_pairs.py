"""
https://leetcode.com/problems/swap-nodes-in-pairs/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: #Time complexity O(n), Space complexity O(1)
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = dummy.next

        while curr and curr.next:
            #save ptrs
            nxt = curr.next
            tmp = curr.next.next

            #reverse cur pair
            nxt.next = curr
            curr.next = tmp
            prev.next = nxt

            #update ptrs
            prev = curr
            curr = curr.next

        return dummy.next