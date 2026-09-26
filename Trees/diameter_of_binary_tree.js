/*
https://leetcode.com/problems/diameter-of-binary-tree/description/
*/


/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     * Time complexity O(n), Space complexity O(n)
     */
    diameterOfBinaryTree(root) {
        let res = 0

        function dfs(node){
            if(!node){
                return -1
            }

            let left = 1 + dfs(node.left)
            let right = 1 + dfs(node.right)

            res = Math.max(res, left + right)
            return Math.max(left, right)
        }

        dfs(root)

        return res
    }
}
