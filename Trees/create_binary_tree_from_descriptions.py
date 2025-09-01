"""
https://leetcode.com/problems/create-binary-tree-from-descriptions/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: #Time complexity O(n), Space complexity O(n)
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashmap = {} #value: [Node, hasParent]

        for parent, child, isLeft in descriptions:
            if parent not in hashmap:
                hashmap[parent] = [TreeNode(parent), False]
            
            if child not in hashmap:
                hashmap[child] =  [TreeNode(child), True]
            else:
                hashmap[child][1] = True

            if isLeft:
                hashmap[parent][0].left = hashmap[child][0]
            else:
                hashmap[parent][0].right = hashmap[child][0]


        for node, hasParent in hashmap.values():
            if not hasParent:
                return node

        
