/*
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
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
    maxDepth(root) {
        if(root === null){
            return 0
        }

        return 1 + Math.max(this.maxDepth(root.left), this.maxDepth(root.right))
    }
}
