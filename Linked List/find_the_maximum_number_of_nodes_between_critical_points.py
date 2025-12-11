"""
https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        points = []
        cur = head.next
        prev = head
        i = 1

        while cur and cur.next:
            if prev.val < cur.val and cur.val > cur.next.val:
                points.append(i)
            elif prev.val > cur.val and cur.val < cur.next.val:
                points.append(i)

            prev = cur
            cur = cur.next
            i += 1


        maxD = points[-1] - points[0] if len(points) > 1 else -1
        minD = math.inf

        for i in range(1, len(points)):
            minD = min(minD, points[i] - points[i-1])


        minD = minD if minD != math.inf else -1

        return [minD, maxD]



        

            

        
