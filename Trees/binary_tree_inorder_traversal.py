"""
https://leetcode.com/problems/binary-tree-inorder-traversal/description/
"""

class RecursiveSolution: #Time complexity O(n), Space complexity O(n)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = [] #behaves as a global variable to the inorder function

        def inorder(root):
            if not root:
                return  #pops back to the parent node
        
            inorder(root.left) #inorder the left sub-tree
            res.append(root.val)
            inorder(root.right) #inorder the right sub-tree

        inorder(root)
        return 
    
class IterativeSolution: #Time complexity O(n), Space complexity O(n)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            while curr: # not "curr.left"
                stack.append(curr)
                curr = curr.left
            curr = stack.pop() #allow the stack to be popped even if curr is null
            res.append(curr.val)
            curr = curr.right #this will always get called if curr.left is null

        return res
