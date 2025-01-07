"""
https://leetcode.com/problems/even-odd-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Time complexity O(n), Space complexity O(n)
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = -1

        while q:
            level += 1
            if level % 2 == 0:
                prev = -math.inf
                even = True
            else:
                prev = math.inf
                even = False

            for i in range(len(q)):
                node = q.popleft()

                if ((even and (node.val <= prev or node.val % 2 == 0)) or 
                (not even and (node.val >= prev or node.val % 2 != 0))) :
                    return False

                prev = node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return True

class CleanerSolution: #Same complexity as above
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        even = True

        while q:
            prev = -math.inf if even else math.inf

            for i in range(len(q)):
                node = q.popleft()

                if ((even and (node.val <= prev or node.val % 2 == 0)) or 
                (not even and (node.val >= prev or node.val % 2 != 0))) :
                    return False

                prev = node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            even = not even


        return True

            
                
        

            
                
        
