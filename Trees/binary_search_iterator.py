# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class MyBSTIterator: #Time complexity O(n), Space complexity O(1)

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack.pop()
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left

        return res.val
        
    def hasNext(self) -> bool:
        return len(self.stack) != 0

class BSTIterator: #Time complexity O(h), Space complexity O(1)

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root: #so initially we go as far left as possible to land on the lowest value, we only need to go right when next() is needed
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack.pop()
        cur = res.right #we slide right once, and then go as far to the left again
        while cur:
            self.stack.append(cur)
            cur = cur.left

        return res.val
        
    def hasNext(self) -> bool:
        return len(self.stack) != 0 #as the stack is non-empty we can be sure there's a right because that indicates there's a larger value to consider
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
