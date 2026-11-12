/*
https://leetcode.com/problems/same-tree/description/
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
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     * Time complexity O(p + q), Space complexity O(p + q)
     */
    isSameTree(p, q) {
        if(!p && !q){
            return true
        }else if(p && q){
            return (p.val === q.val) && this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right)
        }else{
            return false
        }
    }
}
