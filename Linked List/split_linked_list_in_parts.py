"""
https://leetcode.com/problems/split-linked-list-in-parts/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MySolution: #Time complexity is O(max(n, k)), Space complexity O(k + n)
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        counts = [0 for i in range(k)]
        res  = []

        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        idx = 0

        for i in range(length): #to distribute the length as evenly as possible
            counts[idx % k] += 1
            idx += 1

        dummy = ListNode(None, head)
        currhead = head
        currtail = dummy
        for count in counts:
            if not count: #if count is 0 that means no nodes need tp be added
                res.append(None)
                continue
            
            while count: #for each part we have a count that's used to determine the where the tail of the linked list should be
                currtail = currtail.next
                count -= 1
            tmp = currtail.next 
            currtail.next = None
            res.append(currhead)
            currhead = tmp
            dummy.next = currhead #a dummy node is needed for edge cases of only 1 node being added for instance
            currtail = dummy

        return res

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class CleanerSolution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res = []
        length = 0
        curr = head

        while curr:
            curr = curr.next
            length += 1

        baseLen = length//k #baselen tells us the minimum len needed in each part
        rem = length % k # rem tells us the extras that need to be added from the front parts
        curr = head

        for i in range(k):
            res.append(curr) #start by appending the head of the part

            for i in range(baseLen - 1 + (1 if rem else 0)): #starting from head, baselen - 1 determines the minimum number of steps to reach the tail, a 1 is added if there a remainders
                if not curr: break #we've already appended the head (None) so we can continue on
                curr = curr.next
            rem -= 1 if rem else 0 #if we've used up rem, it should remain at zero
            if curr:
                curr.next, curr = None, curr.next #to define the tail of a part and simultaneously move to the next part 

        return res

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MyOtherSolution: #Cleaner version of my first solution
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        counts = [0 for i in range(k)]

        i = 0
        cur = head

        while cur:
            counts[i] += 1
            i += 1
            if i == len(counts):
                i = 0
            cur = cur.next

        start = head
        end = head
        res = [None for i in range(k)]
        i = 0

        while end:
            while counts[i] - 1:
                end = end.next
                counts[i] -= 1
            temp = end.next
            end.next = None
            res[i] = start
            start = temp
            end = temp
            i += 1

        return res

        



        
