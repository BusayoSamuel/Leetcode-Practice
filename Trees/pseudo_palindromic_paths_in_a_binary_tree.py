"""
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class MySolution: #Time complexity O(n * k) due to check function, Space complexity O(h + k) where n is the number of nodes and k is the max number of unique nodes and h is the hegiht of the tree
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        hashmap = {}

        def check():
            flag = True
            for key, value in hashmap.items():
                if value % 2 != 0:
                    if not flag:
                        return False
                    flag = not flag
            
            return True


        res = 0

        def dfs(node):
            nonlocal res 

            if not node:
                return

            hashmap[node.val] = hashmap.get(node.val, 0) + 1

            if not node.left and not node.right:
                if check():
                    res += 1
            else:
                dfs(node.left)
                dfs(node.right)
                
            hashmap[node.val] -= 1
            if hashmap[node.val] == 0:
                del hashmap[node.val]


        dfs(root)
        return res

class CleanerSolution: #Time complexity O(n), Space complexity O(h + k)
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = defaultdict(int)
        odd = 0

        def dfs(curr):
            nonlocal odd

            if not curr:
                return 0

            count[curr.val] += 1
            odd_change = 1 if count[curr.val] % 2 else -1
            odd += odd_change

            if not curr.left and not curr.right:
                res = 1 if odd <= 1 else 0
            else:
                res = dfs(curr.left) + dfs(curr.right)
            
            odd -= odd_change
            count[curr.val] -= 1

            return res

        return dfs(root)

            



        
        
