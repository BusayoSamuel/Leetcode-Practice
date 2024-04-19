"""
https://leetcode.com/problems/maximum-width-of-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Time complexity O(n), Space complexity O(n) not as efficient in memory
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()

        if root:
            q.append(root)

        res = 0

        while q:
            foundFirst = False
            foundLast = False
            allNull = True
            count = 0


            for i in range(len(q)):
                node = q.popleft()

                if not node: #the extea null values are stores which increases memory usage inefficiently
                    q.append(None)
                    q.append(None)
                else:
                    allNull = False
                    if foundFirst or not q:
                        foundLast = True
                    foundFirst = True
                    q.append(node.left)
                    q.append(node.right)
                
                if foundFirst:
                    count+=1
                
                if foundLast:
                    res = max(res, count)
                    foundLast = False

            
            if allNull: break


        return res



class OptimalSolution: #Time complexity O(n) Space complexity O(n)
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()

        if root:
            q.append((root,1,0)) #(node, number, level)

        prevNum = 1
        prevLevel = 0

        res = 0

        while q:

            for i in range(len(q)):
                node, num, level = q.popleft()

                if prevLevel < level:
                    prevNum = num
                    prevLevel = level

                res = max(res, num-prevNum+1)   

                if node.left:
                    q.append((node.left, num * 2, level + 1))

                if node.right:
                    q.append((node.right, num * 2 + 1, level + 1))

            
        return res
