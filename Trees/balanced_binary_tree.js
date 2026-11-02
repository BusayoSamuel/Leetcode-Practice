/*
https://leetcode.com/problems/balanced-binary-tree/description/
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
     * @return {boolean}
     * Time complexity O(n), Space complexity O(n)
     */
    isBalanced(root) {
        function dfs(node){
            if(!node){
                return [0, true]
            }

            const [lHeight, lBal] = dfs(node.left)
            const [rHeight, rBal] = dfs(node.right)

            if(Math.abs(lHeight - rHeight) > 1){
                return [1 + Math.max(lHeight, rHeight), false]
            }else{
                return [1 + Math.max(lHeight, rHeight), lBal && rBal]
            }
        }

        return dfs(root)[1]
    }
}
