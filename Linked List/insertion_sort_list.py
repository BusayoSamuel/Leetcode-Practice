"""
https://leetcode.com/problems/insertion-sort-list/submissions/1195740827/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MySolution: #Time complexity O(n^2), Space complexity O(1)
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float("-inf"), head) #setting max negative inf allows for comparisons
        head = dummy #head of the sorted portion
        tail = head #tail of the sorted portion

        while tail.next:#we it's sorted if tail has reached the end
            curUnsort = tail.next #the start of the unsorted portion
            prevUnsort = tail 
            curSort = head #the start of the sorted portion
            prevSort = None

	    #checks if the curnode is already sorted
            if curUnsort.val >= tail.val:
                    tail = tail.next
                    continue

	    #check for values that need to be inserted within the sorted portion
            while curSort != tail:
                if curUnsort.val <= curSort.next.val and (curSort.val <= curUnsort.val):
                    prevUnsort.next = prevUnsort.next.next
                    tmp = curSort.next
                    curSort.next = curUnsort
                    curUnsort.next = tmp
                    break
                
                prevSort = curSort
                curSort = curSort.next

        return dummy.next
                     
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #Same complexity, cleaner code
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = head
        cur = head.next #skips the first node because it's sorted already

        while cur: #once cur goes beyond linked list to none, then we know we've sorted every node in the list
	    #check if cur node is already sorted	    
            if cur.val >= prev.val:
                prev = cur
                cur = cur.next
                continue

            tmp = dummy
            # find a value that is JUST less than cur node
            while cur.val > tmp.next.val:
                tmp = tmp.next

            prev.next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = prev.next

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MyOtherSolution: #Same complexity
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-math.inf, head)
        sort = dummy.next
        unsort = sort.next

        while sort and sort.next:
            if sort.val <= sort.next.val:
                sort = sort.next
                continue

            cur = dummy

            temp = sort.next
            sort.next = sort.next.next

            while cur != sort and cur.val <= cur.next.val <= temp.val:
                cur = cur.next


            nxt = cur.next
            cur.next = temp
            cur.next.next = nxt            

        return dummy.next



        



        
